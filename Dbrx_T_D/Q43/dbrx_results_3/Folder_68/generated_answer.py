def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(lst):
    if len(lst) < 6:
        return []
    primes = [lst[1], lst[2], lst[3], lst[4]]
    for num in primes:
        if not is_prime(num):
            primes.remove(num)
    primes = sorted(list(set(primes)))
    return primes