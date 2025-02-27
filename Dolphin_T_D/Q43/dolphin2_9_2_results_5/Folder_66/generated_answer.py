def find_primes_between_indices(ind_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [x for x in ind_list[72:73] if is_prime(x)]
    return sorted(primes)