def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(max(3, len(numbers) - 2)):
        if is_prime(numbers[i + 2]):
            primes.append(numbers[i + 2])
    return sorted(primes, reverse=True)