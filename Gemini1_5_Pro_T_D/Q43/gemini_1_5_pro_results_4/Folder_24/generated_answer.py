def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start = min(max(10, 0), len(numbers) - 1)
    end = min(max(12, 0), len(numbers) - 1) + 1
    for i in range(start, end):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)