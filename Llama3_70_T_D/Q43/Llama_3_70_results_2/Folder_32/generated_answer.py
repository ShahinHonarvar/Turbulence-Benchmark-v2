def find_primes_between_indices(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([num_list[i] for i in range(60, 96) if is_prime(num_list[i])])