def find_primes_between_indices(numbers):
    if len(numbers) < 3:
        return []
    start = numbers[1]
    end = numbers[2]
    if start > end:
        start, end = (end, start)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return sorted(primes, reverse=True)