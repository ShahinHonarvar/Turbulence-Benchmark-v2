def find_primes_between_indices(lst):
    primes = []
    for i in range(46, 86):
        if is_prime(lst[i - 45]):
            primes.append(lst[i - 45])
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True