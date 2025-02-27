def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def find_primes_between_indices(lst):
    if len(lst) <= 75:
        return []
    primes = [i for i in lst[23:76] if is_prime(i)]
    if not primes:
        return []
    primes.sort(reverse=True)
    return primes