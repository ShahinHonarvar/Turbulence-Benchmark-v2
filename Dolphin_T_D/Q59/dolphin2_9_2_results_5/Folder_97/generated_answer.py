def is_prime(n):
    if n == 1:
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

def all_left_truncatable_prime(t):
    x = t[645]
    primes = [2]
    for i in range(3, x):
        if is_prime(i):
            n = i
            while n != 0 and is_prime(n):
                n //= 10
            if n == 0:
                primes.append(i)
    primes.sort()
    return primes