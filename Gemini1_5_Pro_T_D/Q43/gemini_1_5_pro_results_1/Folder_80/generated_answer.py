def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start_index = 84
    end_index = 84
    if 0 <= start_index <= end_index < len(numbers):
        for i in range(start_index, end_index + 1):
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    return sorted(primes)