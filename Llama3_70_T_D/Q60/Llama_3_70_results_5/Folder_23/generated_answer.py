def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = [i for i in range(2, x + 1) if truncatable(i) and is_prime(i)]
    return sorted(truncatable_primes, reverse=True)