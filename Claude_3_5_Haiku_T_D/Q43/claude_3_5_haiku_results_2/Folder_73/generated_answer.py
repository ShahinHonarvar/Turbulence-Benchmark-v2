def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) <= 90:
        return []
    prime_numbers = [num for num in numbers[19:91] if is_prime(num)]
    return sorted(prime_numbers, reverse=True)