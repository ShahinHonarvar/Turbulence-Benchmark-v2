def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    start_index = 13
    end_index = 68
    for i in range(start_index, end_index + 1):
        if i >= len(numbers):
            break
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes