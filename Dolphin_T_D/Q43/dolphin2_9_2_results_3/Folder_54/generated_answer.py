def find_primes_between_indices(int_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([int_list[i] for i in range(13, 64) if is_prime(int_list[i])])