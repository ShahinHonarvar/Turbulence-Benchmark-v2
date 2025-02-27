def find_primes_between_indices(numbers):
    primes = [x for x in sorted(set(numbers))[76:93] if is_prime(x)]
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True