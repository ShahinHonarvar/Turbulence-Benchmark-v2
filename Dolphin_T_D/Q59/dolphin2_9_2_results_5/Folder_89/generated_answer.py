def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(t):
    x = t[97]
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and (not '0' in str(i)) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))]
    return sorted(left_truncatable_primes, reverse=True)