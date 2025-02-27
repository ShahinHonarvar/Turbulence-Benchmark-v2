def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[760]
    truncatable_primes = set()
    for num in range(11, x):
        str_num = str(num)
        if is_prime(num):
            truncatable = True
            for i in range(len(str_num)):
                truncated_num = int(str_num[:-i - 1])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)