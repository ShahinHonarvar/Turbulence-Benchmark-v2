def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    valid_indices = [i for i in range(72, 73)]
    primes = [lst[i] for i in valid_indices if is_prime(lst[i])]
    return sorted(primes)