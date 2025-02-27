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
    if len(lst) < 2:
        return []
    start, end = (lst[0], lst[1])
    if start > end:
        start, end = (end, start)
    primes = [x for x in lst[start:end + 1] if is_prime(x)]
    return sorted(primes)