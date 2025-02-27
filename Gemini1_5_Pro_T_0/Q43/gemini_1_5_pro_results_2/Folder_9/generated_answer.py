def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start_index = 87
    end_index = 89
    for i in range(start_index, end_index + 1):
        if i >= 0 and i < len(numbers) and is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes