def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start_index = min(max(10, 0), len(numbers) - 1)
    end_index = min(max(66, 0), len(numbers) - 1)
    for i in range(start_index, end_index + 1):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes