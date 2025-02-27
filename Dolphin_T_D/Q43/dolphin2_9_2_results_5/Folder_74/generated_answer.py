def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(lst):
    return sorted([x for x in lst[23:76] if is_prime(x)], reverse=True)