def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = []
    for i in range(75, 86):
        if i < len(numbers) and is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
    return sorted(prime_numbers)