def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    num_str = str(num)
    while num_str:
        if not is_prime(int(num_str)) or '0' in num_str:
            return False
        num_str = num_str[1:]
    return True

def all_left_truncatable_prime(t):
    if len(t) < 5:
        return []
    x = t[4]
    left_truncatable_primes = [n for n in range(1, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes)