def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [x for x in lst[45:81] if is_prime(x)]
    return sorted(primes, reverse=True)