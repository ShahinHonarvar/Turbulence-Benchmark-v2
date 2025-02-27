def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([numbers[i] for i in range(415, 648) if is_prime(numbers[i])])