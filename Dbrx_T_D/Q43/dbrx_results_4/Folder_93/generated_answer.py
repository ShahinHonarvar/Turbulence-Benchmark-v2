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
    if len(lst) < 72:
        return []
    primes = []
    for i in range(70, 72):
        num = lst[i]
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)