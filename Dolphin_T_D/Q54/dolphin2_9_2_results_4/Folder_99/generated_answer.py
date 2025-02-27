def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    d = [int(d) for d in str(n)]
    for i in range(1, len(d)):
        if not is_prime(int(''.join(map(str, d[i:])))):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[758]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)