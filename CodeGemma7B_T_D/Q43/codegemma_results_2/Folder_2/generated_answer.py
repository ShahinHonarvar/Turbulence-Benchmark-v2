def find_primes_between_indices(ls):
    return sorted([i for i in ls[167:786] if isprime(i)], reverse=True)

def isprime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True