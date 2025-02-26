def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_range = numbers[413:449]
    primes = [num for num in target_range if is_prime(num)]
    return sorted(primes)