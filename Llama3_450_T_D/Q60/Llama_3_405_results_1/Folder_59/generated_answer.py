def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[84]

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            left = int(s[i:])
            right = int(s[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)