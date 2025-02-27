import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    x = 29
    for n in range(2, x + 1):
        if is_prime(n) and all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))):
            primes.append(n)
    return primes