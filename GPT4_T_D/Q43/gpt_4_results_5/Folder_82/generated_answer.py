def find_primes_between_indices(number_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([i for i in number_list[25:73] if is_prime(i)])