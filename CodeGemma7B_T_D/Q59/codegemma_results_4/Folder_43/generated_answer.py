from math import sqrt

def prime_checker(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def lefttrunc_checker(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        current = int(str_num[i:])
        if not prime_checker(current):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[89]
    result = []
    for i in range(2, x):
        if prime_checker(i) and lefttrunc_checker(i):
            result.append(i)
    return sorted(result, reverse=True)