def find_primes_between_indices(num_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num_list[i] for i in range(61, 81) if is_prime(num_list[i])]
    return sorted(primes, reverse=True)