import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    if x < 10:
        return []
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            while len(str_i) > 1:
                str_i = str_i[1:-1]
                if str_i[0] == '0' or str_i[1] == '0':
                    break
                if not is_prime(int(str_i)):
                    break
                if len(str_i) == 2:
                    primes.append(i)
    primes.sort(reverse=True)
    return primes