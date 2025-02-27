import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and i % 10 > 0 and (i != 2) and (i != 3) and (i != 5) and (i != 7):
            trunc_i = i
            while trunc_i >= 10:
                trunc_i = int(str(trunc_i)[1:-1])
                if not is_prime(trunc_i):
                    break
            else:
                primes.append(i)
    return primes