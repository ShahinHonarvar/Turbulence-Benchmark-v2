def find_primes_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([num_list[i] for i in range(len(num_list)) if 87 <= i <= 89 and is_prime(num_list[i])])