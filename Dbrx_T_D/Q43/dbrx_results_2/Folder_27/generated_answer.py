def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(numbers):
    primes = [x for x in numbers[11:12] if is_prime(x)]
    primes.sort()
    return primes