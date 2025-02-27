from itertools import count

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

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_left_truncatable_prime(tup):
    prime_numbers = []
    for i in count(1):
        x = int(str(i) + str(list(tup)[94]))
        if is_left_truncatable_prime(x):
            prime_numbers.append(x)
        if x > list(tup)[94]:
            break
    return sorted(prime_numbers)