from math import sqrt

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

def right_truncatable_prime(x):
    for i in range(2, x):
        if is_prime(i):
            number = i
            while number != 0:
                number //= 10
                if not is_prime(number):
                    break
            else:
                return [i]
    return []