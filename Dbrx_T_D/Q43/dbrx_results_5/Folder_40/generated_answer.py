def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(1, min(len(numbers), 2)):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)