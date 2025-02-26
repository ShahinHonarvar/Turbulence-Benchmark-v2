def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start = 19
    end = min(72, len(numbers))
    primes = []
    for i in range(start, end):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)