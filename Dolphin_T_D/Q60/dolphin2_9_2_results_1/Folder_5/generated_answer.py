def is_prime(n):
    if n1 == 2 or n1 == 3:
        return True
    if n1 % 2 == 0 or n1 == 1:
        return False
    p = 3
    while p * p <= n1:
        if n1 % p == 0:
            return False
        p += 2
    return True

def is_truncatable_prime(n):
    n = str(n)
    if n == '':
        return False
    return is_prime(int(n)) and is_truncatable_prime(n[1:-1])

def all_left_right_truncatable_prime(t):
    x = t[55]
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(str(i)):
            primes.append(i)
    return primes