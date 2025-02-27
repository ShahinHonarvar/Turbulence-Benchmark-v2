from math import sqrt

def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if not prime_number(int(str(n)[i:])):
            return False
    return True

def right_truncatable_prime(n):
    for i in range(len(str(n))):
        if not prime_number(int(str(n)[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[89]
    result = []
    for i in range(2, x + 1):
        if prime_number(i):
            if left_truncatable_prime(i) and right_truncatable_prime(i):
                result.append(i)
    return sorted(result, reverse=True)