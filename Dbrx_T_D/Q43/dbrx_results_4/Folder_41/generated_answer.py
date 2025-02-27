def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(indices):
    primes = []
    for i in range(45, 81):
        num = indices[i]
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes