def find_primes_between_indices(integer_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([integer_list[i] for i in range(len(integer_list)) if is_prime(integer_list[i]) and 1 <= i <= 1])