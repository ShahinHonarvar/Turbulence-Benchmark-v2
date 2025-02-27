def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    start_index = 19
    end_index = 71
    for index in range(start_index, end_index + 1):
        if index < len(numbers) and is_prime(numbers[index]):
            primes.append(numbers[index])
    primes.sort()
    return primes