def find_primes_between_indices(array):
    result = []
    for i in range(10, 13):
        if is_prime(array[i]):
            result.append(array[i])
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if i % n == 0:
            return False
        i += 2
    return True