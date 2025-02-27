def find_primes_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrtn = int(n ** 0.5) + 1
        for divisor in range(3, sqrtn, 2):
            if n % divisor == 0:
                return False
        return True
    return sorted([num_list[i] for i in range(15, 72) if is_prime(num_list[i])])