def is_prime_n(n):
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
    return [n for n in lst[459:782] if is_prime_n(n)][::-1]