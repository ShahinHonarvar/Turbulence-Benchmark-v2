def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 24
    end_index = 83
    primes = []
    for num in numbers[start_index:end_index + 1]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)