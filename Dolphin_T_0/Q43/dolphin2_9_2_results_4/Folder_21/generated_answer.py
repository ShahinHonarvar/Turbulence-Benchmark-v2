def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    return sorted([x for x in lst[478:950] if is_prime(x)], reverse=True)