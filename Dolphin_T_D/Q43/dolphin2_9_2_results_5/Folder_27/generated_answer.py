def find_primes_between_indices(num_list):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted(list(filter(is_prime, num_list[11:12])))