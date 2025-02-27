def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    n = len(str(x))
    primes, right_truncatables = ([], [])
    for i in range(1, 10 ** n):
        if is_prime(i):
            primes.append(i)
    for prime in primes:
        trunc = prime
        while trunc:
            if trunc != prime and is_prime(trunc):
                right_truncatables.append(trunc)
            trunc //= 10
    return sorted(right_truncatables)