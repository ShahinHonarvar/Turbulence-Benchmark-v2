def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i >= 28 and i <= 36:
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    primes.sort()
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True