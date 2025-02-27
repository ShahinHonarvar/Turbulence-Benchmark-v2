def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    if len(lst) < 2:
        return []
    start, end = (lst[0], lst[1])
    if start > end:
        start, end = (end, start)
    primes = [x for x in range(start, end + 1) if is_prime(x)]
    return sorted(primes)