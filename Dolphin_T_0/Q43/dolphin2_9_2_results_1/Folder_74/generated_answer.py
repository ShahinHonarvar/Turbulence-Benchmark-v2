def is_prime(n):
    if n < 2:
        return False
    for i in range(2, round(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    return sorted([i for i in lst[23:76] if is_prime(i)], reverse=True)