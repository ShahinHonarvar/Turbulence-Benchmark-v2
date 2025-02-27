def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(numbers):
    if len(numbers) <= 1:
        return []
    primes = [num for num in numbers[0:2] if is_prime(num)]
    for i in range(2, len(numbers)):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)