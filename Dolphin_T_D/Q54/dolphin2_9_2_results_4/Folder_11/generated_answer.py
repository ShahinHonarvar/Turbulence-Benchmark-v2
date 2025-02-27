def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def remove_rightmost_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[86]
    primes = [2]
    i = 3
    while i < x:
        if is_prime(i) and all((is_prime(remove_rightmost_digit(i)) for j in range(len(str(i)) - 1))):
            primes.append(i)
        i += 1
    return sorted(primes) if primes else []