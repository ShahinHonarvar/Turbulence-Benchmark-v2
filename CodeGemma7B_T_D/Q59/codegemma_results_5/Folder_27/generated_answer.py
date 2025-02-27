def leftmost(n):
    while n >= 10:
        n //= 10
    return n

def lefttruncatable_prime(n):
    for d in range(n):
        if isprime(d) and (not contains_zero(d)) and isprime(leftmost(d)):
            yield d

def all_left_truncatable_prime(n):
    f = lefttruncatable_prime(n)
    return sorted(f, reverse=True)

def isprime(n):
    m = int(n ** 0.5) + 2
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True if n >= 2 else False

def contains_zero(d):
    return d == 0