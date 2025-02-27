def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def find_primes_between_indices(lst):
    prime_numbers = [lst[i] for i in range(28, 84) if is_prime(lst[i])]
    return sorted(prime_numbers)