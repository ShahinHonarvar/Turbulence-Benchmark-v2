def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [numbers[i] for i in range(229, 851) if is_prime(numbers[i])]
    return sorted(primes, reverse=True)