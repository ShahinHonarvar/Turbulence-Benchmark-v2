def find_primes_between_indices(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5)
        for d in range(3, 1 + max_divisor, 2):
            if n % d == 0:
                return False
        return True
    return sorted([num for num in numbers[29:98] if is_prime(num)], reverse=True)