def find_primes_between_indices(numb_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([numb_list[i] for i in range(59, 98) if is_prime(numb_list[i])], reverse=True)