def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def all_right_truncatable_prime(t):
    x = t[77]
    primes = [i for i in t if is_right_truncatable(i)]
    primes = [i for i in primes if i < x]
    return sorted(primes)