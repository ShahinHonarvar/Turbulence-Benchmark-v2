def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start = 55
    end = 76
    if len(numbers) >= end + 1:
        for i in range(start, end + 1):
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    primes.sort()
    return primes