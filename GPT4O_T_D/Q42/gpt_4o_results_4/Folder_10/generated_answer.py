def prime_factors(lst):

    def get_primes(num):
        primes = set()
        i = 2
        while i * i <= num:
            while num % i == 0:
                primes.add(i)
                num //= i
            i += 1
        if num > 1:
            primes.add(num)
        return primes
    if len(lst) > 54:
        return get_primes(lst[54])
    return set()