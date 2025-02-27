def find_primes_between_indices(numbers):
    primes = []
    for i in range(37, 96):
        number = numbers[i]
        if is_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True