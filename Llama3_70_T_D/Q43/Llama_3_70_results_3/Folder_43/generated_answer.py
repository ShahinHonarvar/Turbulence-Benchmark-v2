import math

def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    primes_in_range = [numbers[i] for i in range(31, 93) if is_prime(numbers[i])]
    return sorted(primes_in_range, reverse=True)