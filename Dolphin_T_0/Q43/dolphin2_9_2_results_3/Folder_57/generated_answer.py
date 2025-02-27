def find_primes_between_indices(num_list):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    prime_list = [num for num in num_list[35:90] if is_prime(num)]
    return sorted(prime_list, reverse=True)