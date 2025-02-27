def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    if len(t) < 92:
        return []
    x = t[91]
    truncatable_primes = []
    for n in range(10, x + 1):
        if is_prime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    return truncatable_primes