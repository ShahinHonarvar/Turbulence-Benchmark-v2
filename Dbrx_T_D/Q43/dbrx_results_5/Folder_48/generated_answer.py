def find_primes_between_indices(numbers):
    prime_indices = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i, number in enumerate(numbers):
        if i >= 261 and i <= 459 and is_prime(number):
            prime_indices.append(number)
    return sorted(prime_indices)