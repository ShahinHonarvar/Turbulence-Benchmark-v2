import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[126]
    primes = []
    for i in range(x, 1, -1):
        str_i = str(i)
        if '0' in str_i:
            continue
        trunc = len(str_i)
        while trunc > 0:
            if not is_prime(int(str_i[trunc - 1:])):
                break
            trunc -= 1
        if trunc == 0:
            primes.append(i)
    return sorted(primes, reverse=True)