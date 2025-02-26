def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes_in_range = [num for num in numbers[56:58] if is_prime(num)]
    return sorted(primes_in_range, reverse=True)