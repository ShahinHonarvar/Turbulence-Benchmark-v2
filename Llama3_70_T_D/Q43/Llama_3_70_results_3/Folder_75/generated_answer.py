def find_primes_between_indices(num_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([num_list[i] for i in range(46, 62) if is_prime(num_list[i])])