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
    if n <= 1:
        return False
    if n <= 9:
        return True
    n_str = str(n)
    i, j = (len(n_str) - 1, 0)
    while i > j:
        if n_str[j] == '0' or n_str[i] == '0':
            return False
        if not is_prime(int(n_str[j:i + 1])):
            return False
        i -= 1
        j += 1
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[126]
    primes = []
    for n in range(x, 1, -1):
        if is_truncatable(n) and is_prime(n):
            primes.append(n)
    return primes