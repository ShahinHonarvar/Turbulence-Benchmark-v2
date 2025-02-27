def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[30]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            j = i
            while j > 1:
                j //= 10
                if not is_prime(j):
                    break
            else:
                primes.append(i)
    primes.sort(reverse=True)
    return primes if primes else []