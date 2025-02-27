def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    numbers_slice = numbers[3:9]
    primes = [num for num in numbers_slice if is_prime(num)]
    return sorted(primes)