def prime_factors(lst):

    def find_prime_factors(n):
        primes = set()
        while n % 2 == 0:
            primes.add(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                primes.add(i)
                n //= i
        if n > 2:
            primes.add(n)
        return primes
    if 0 <= 926 < len(lst) and isinstance(lst[926], int) and (lst[926] > 0):
        return find_prime_factors(lst[926])
    return set()