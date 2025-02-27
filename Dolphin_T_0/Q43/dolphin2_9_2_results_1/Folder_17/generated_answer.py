def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [numbers[i] for i in range(len(numbers)) if 15 <= i <= 48 and is_prime(numbers[i])]
    return sorted(primes, reverse=True)