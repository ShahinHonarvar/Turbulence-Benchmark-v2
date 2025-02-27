def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([num for i, num in enumerate(numbers) if 430 <= i <= 805 and is_prime(num)])