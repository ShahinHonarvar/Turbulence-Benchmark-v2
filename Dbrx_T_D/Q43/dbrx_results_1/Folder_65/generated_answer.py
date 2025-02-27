def find_primes_between_indices(lst):
    primes = []
    for i in range(len(lst)):
        if i >= 76 and i <= 92:
            if is_prime(lst[i]):
                primes.append(lst[i])
    primes.sort()
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True