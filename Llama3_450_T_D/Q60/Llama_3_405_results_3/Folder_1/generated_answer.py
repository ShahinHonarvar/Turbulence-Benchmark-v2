def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    truncatable_primes = set()
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        if is_prime(num):
            truncatable = True
            for i in range(1, len(num_str)):
                trunc_left = int(num_str[i:])
                trunc_right = int(num_str[:-i])
                if not is_prime(trunc_left) or not is_prime(trunc_right):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)