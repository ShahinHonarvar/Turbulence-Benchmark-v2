from math import sqrt

def prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

def digits(n):
    return [int(d) for d in str(n)]

def is_left_truncatable_prime(n):
    num_digits = len(digits(n))
    for i in range(1, num_digits):
        if not prime(int(str(n)[:i])):
            return False
    return prime(n)

def all_left_truncatable_prime(x):
    x = digits(x)[88]
    result = []
    for i in range(x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)