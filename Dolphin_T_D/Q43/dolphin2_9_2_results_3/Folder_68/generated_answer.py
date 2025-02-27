def find_primes_between_indices(numbers):
    list_of_primes = []

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return num > 1
    for i in range(1, 6):
        if is_prime(numbers[i]):
            list_of_primes.append(numbers[i])
    return sorted(list_of_primes)