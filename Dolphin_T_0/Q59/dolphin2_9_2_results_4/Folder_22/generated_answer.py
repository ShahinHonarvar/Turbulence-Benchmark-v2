def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[85]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_left_truncatable(n):
    if n % 10 == 0:
        return False
    while n > 0:
        if check_prime(n):
            n //= 10
        else:
            return False
    return True

def check_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True