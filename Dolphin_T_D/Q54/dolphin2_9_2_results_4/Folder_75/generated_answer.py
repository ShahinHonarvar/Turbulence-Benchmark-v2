def all_right_truncatable_prime(integers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, primes):
        if n not in primes:
            return False
        return all((is_prime(n // 10 ** i) for i in range(1, len(str(n)))))
    x = integers[41]
    primes = [2]
    if x < 2:
        return []
    i = 3
    while i <= x:
        if is_prime(i):
            primes.append(i)
        i += 2
    return sorted([n for n in primes if is_truncatable_prime(n, primes)])