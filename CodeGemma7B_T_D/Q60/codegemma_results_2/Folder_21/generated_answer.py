from math import sqrt

def is_prime(number):
    if number < 2:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def left(n):
    if n < 10:
        return n
    return int(str(n)[:-1])

def right(n):
    if n < 10:
        return n
    return int(str(n)[-1])

def factorize(n):
    factors = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def has_zero(n):
    return '0' in str(n)

def all_left_right_truncatable_prime(tup):
    x = tup[175]
    result = []
    for n in range(2, x + 1):
        if not has_zero(n) and is_prime(n):
            temp = n
            while temp > 1 and is_prime(temp):
                if right(temp) <= 3 and (left(temp) == right(temp) or left(temp) == 2):
                    if is_prime(left(temp)):
                        result.append(n)
                        break
                temp = left(temp)
    return sorted(result)