def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start = 11
    end = 11
    result = []
    if len(numbers) <= start:
        return result
    for i in range(start, min(end + 1, len(numbers))):
        if is_prime(numbers[i]):
            result.append(numbers[i])
    return sorted(result)