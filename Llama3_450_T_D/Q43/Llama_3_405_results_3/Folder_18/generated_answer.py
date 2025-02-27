def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = [num for idx, num in enumerate(numbers) if 430 <= idx <= 805 and is_prime(num)]
    return sorted(prime_numbers)