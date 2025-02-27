import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_zeros(n):
    str_n = str(n)
    while str_n.startswith('0'):
        str_n = str_n[1:]
    while str_n.endswith('0'):
        str_n = str_n[:-1]
    return int(str_n)

def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(x + 1):
        if is_prime(i):
            truncatable_i = remove_zeros(i)
            if truncatable_i >= 10 and is_prime(truncatable_i):
                primes.append(i)
    return sorted(primes, reverse=True)