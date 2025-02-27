def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in numbers[66:82]:
        if is_prime(i):
            primes.append(i)
    primes.sort()
    return primes