def find_primes_between_indices(lst):
    primes = sorted(set(lst[55:77]))
    primes = [x for x in primes if is_prime(x)]
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True