def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(46, 62):
        curr = lst[i]
        if is_prime(curr):
            primes.append(curr)
    return sorted(primes)