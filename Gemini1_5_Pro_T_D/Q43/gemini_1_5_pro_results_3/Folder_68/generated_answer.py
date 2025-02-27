def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    if len(numbers) >= 3:
        for num in numbers[2:3]:
            if is_prime(num):
                primes.append(num)
    return sorted(primes)