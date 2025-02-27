def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for i, num in enumerate(numbers[3:9]) if is_prime(num)]
    return sorted(primes)