def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if len(numbers) < 287:
        return []
    primes = [num for num in numbers[287:929] if is_prime(num)]
    return sorted(primes)