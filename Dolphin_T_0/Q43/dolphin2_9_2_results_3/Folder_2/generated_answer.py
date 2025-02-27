def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [x for x in lst[166:786] if is_prime(x)]
    return sorted(primes, reverse=True)