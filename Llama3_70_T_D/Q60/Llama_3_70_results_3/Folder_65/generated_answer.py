def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(args):
    limit = args[32]
    truncatable_primes = [i for i in range(11, limit + 1) if '0' not in str(i) and is_prime(i) and is_left_right_truncatable(i)]
    return truncatable_primes