def find_primes_between_indices(numbers):
    start_index = 33
    end_index = 35

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for index in range(start_index, end_index + 1):
        if is_prime(numbers[index]):
            primes.append(numbers[index])
    return sorted(primes)