import math

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

def is_truncatable(n):
    num = n
    while len(str(num)) > 1:
        if not is_prime(num):
            return False
        num = num // 10
        if not is_prime(num):
            return False
    return True

def all_left_right_truncatable_prime(num_list):
    x = num_list[126]
    primes = []
    for i in range(x, 1, -1):
        if is_truncatable(i):
            primes.append(i)
    return primes