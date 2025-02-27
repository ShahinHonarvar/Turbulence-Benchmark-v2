def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    start_index = 52
    end_index = 53
    if len(numbers) > end_index:
        for i in range(start_index, end_index + 1):
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    primes.sort()
    return primes