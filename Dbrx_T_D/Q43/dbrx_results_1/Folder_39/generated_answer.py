def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i < 69 or i > 80:
            continue
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(list(set(primes)))

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