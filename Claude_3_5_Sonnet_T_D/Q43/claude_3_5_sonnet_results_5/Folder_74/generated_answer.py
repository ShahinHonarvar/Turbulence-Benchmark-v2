def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start = max(23, 0)
    end = min(76, len(numbers))
    primes = [num for num in numbers[start:end] if is_prime(num)]
    return sorted(primes, reverse=True)