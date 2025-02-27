def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    primes = [num for num in numbers[52:54] if is_prime(num)]
    return sorted(primes)