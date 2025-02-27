def find_primes_between_indices(lst):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    primes = [i for i in lst[35:90] if is_prime(i)]
    return sorted(primes, reverse=True) if primes else []