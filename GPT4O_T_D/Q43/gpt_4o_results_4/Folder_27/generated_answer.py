def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) > 11:
        sublist = numbers[11:12]
        primes = [num for num in sublist if is_prime(num)]
    else:
        primes = []
    return sorted(primes)