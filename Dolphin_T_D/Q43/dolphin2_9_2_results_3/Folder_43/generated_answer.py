def find_primes_between_indices(group_of_ints):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([i for i in group_of_ints[31:93] if is_prime(i)], reverse=True)