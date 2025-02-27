def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start_index = 83
    end_index = 84
    if len(numbers) > end_index:
        for i in range(start_index, end_index + 1):
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    primes.sort()
    return primes