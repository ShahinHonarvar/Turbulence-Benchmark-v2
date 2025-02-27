def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[100]
    primes = []
    for n in range(x, 0, -1):
        if is_prime(n):
            m = n
            while m != 0 and is_prime(m):
                m //= 10
            if m == 0:
                primes.append(n)
    return sorted(primes, reverse=True)