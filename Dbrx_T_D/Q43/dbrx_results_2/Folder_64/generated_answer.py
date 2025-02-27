def find_primes_between_indices(numbers):
    return sorted((x for x in numbers[7:10] if is_prime(x)), reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True