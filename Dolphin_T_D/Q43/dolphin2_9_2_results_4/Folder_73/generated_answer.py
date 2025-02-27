def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(numbers):
    result = [num for num in numbers[19:91] if is_prime(num)]
    return sorted(result, reverse=True)