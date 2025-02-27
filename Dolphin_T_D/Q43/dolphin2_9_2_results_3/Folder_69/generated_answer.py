def find_primes_between_indices(numbers_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [numbers_list[i] for i in range(497, 931) if is_prime(numbers_list[i])]
    return sorted(primes, reverse=True)