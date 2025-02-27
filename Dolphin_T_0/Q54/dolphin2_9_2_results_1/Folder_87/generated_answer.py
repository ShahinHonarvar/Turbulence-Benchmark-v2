def is_prime(n):
    if n in (0, 1):
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
                if j == 0:
                    primes.append(i)
    return sorted(primes, reverse=True)