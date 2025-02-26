def find_primes_between_indices(numbers):
    if len(numbers) < 2:
        return []
    start = min(numbers[0], numbers[1])
    end = max(numbers[0], numbers[1])

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes