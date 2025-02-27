def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i) and is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)