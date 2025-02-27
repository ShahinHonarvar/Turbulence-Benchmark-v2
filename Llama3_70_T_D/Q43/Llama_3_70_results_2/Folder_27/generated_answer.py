def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 11
    end_index = 11
    primes = [lst[i] for i in range(start_index, end_index + 1) if is_prime(lst[i])]
    return sorted(primes)