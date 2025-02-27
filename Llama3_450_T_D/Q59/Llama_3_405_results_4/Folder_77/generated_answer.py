def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    truncatable_primes = set()
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num:
            truncatable = True
            for i in range(len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)