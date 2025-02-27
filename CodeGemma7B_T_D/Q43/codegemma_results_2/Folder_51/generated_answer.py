def find_primes_between_indices(numbers):
    primes = []
    for x in numbers[14:69]:
        if is_prime(x):
            primes.append(x)
    primes.sort(reverse=True)
    return primes

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True