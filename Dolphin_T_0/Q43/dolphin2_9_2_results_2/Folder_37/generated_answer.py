def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    primes = []
    for i in range(13, 69):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes