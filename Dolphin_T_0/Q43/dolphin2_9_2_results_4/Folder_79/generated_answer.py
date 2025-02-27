def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = []
    for n in lst[33:36]:
        if is_prime(n):
            primes.append(n)
    return sorted(primes)