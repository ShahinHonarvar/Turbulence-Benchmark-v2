def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leftmost_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(t):
    x = t[3]
    primes = []
    for n in range(2, x):
        m = n
        while m != 0 and is_prime(m):
            m = remove_leftmost_digit(m)
        if m == 0 and is_prime(n):
            primes.append(n)
    return sorted([i for i in primes if i > 1], reverse=True)