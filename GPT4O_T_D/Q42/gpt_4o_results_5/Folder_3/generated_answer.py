def prime_factors(lst):

    def get_primes(n):
        if n <= 1:
            return set()
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
    if len(lst) > 100:
        target_number = lst[100]
        return get_primes(target_number)
    return set()