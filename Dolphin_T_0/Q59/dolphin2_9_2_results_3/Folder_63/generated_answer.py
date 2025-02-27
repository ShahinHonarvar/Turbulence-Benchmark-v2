def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[88]
    primes = [2, 3, 5, 7]
    if x < 10:
        return primes[:x]
    while primes[-1] < x:
        n = primes[-1] + 1
        while n < x:
            if is_prime(n):
                primes.append(n)
            n += 1
        for p in primes:
            if p < 10 and p in primes:
                primes.remove(p)
            elif p // 10 in primes and p % 10 in primes:
                continue
            else:
                primes.remove(p)
    return primes