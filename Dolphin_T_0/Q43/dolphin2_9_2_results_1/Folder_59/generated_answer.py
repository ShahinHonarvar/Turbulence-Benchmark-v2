def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [x for x in lst[4:9] if is_prime(x)]
    return sorted(primes, reverse=True)