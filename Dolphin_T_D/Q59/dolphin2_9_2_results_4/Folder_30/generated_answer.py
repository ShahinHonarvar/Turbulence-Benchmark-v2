import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[37]
    primes = []
    for i in range(x - 1, 0, -1):
        str_i = str(i)
        if '0' in str_i:
            continue
        while str_i and is_prime(int(str_i)):
            str_i = str_i[1:]
        if str_i == '':
            primes.append(i)
    return sorted(primes, reverse=True)