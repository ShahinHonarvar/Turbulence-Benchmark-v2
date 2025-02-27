def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(numbers):
    primes_in_range = []
    for i in range(33, min(60, len(numbers))):
        if is_prime(numbers[i]):
            primes_in_range.append(numbers[i])
    primes_in_range.sort(reverse=True)
    return primes_in_range