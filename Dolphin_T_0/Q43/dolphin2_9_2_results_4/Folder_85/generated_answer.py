def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(32, 36):
        if is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort()
    return primes