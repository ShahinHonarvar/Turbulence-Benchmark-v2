def all_left_truncatable_prime(t):
    x = t[24]
    primes = [2]
    A = [11, 13, 17, 19, 23]
    for q in A:
        primes.append(q)
        m = primes[-1]
        if all([m // pow(10, i) % 10 != 0 for i in range(1, len(str(m)))]) and all([m // pow(10, i) % 10 != 0 for i in range(len(str(m)))]) and all((i in primes or is_prime(i) for i in [m // pow(10, j) for j in range(len(str(m)))])):
            A = [i for i in A if i != q]
            A.append((m * 10 + a for a in range(10) if m * 10 + a > q and is_prime(m * 10 + a)))
            A = sorted([i for i in A if i > m])
    return sorted([i for i in primes if i < x])

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True