def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(max(0, min(61, len(numbers) - 1)), min(79, len(numbers) - 1) + 1):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes