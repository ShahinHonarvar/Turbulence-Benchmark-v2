def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i >= 295 and i <= 455:
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    primes.sort(reverse=True)
    return primes

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