from math import sqrt

def IsPrime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def IsTruncatablePrime(x):
    str_x = str(x)
    if '0' in str_x:
        return False
    for i in range(1, len(str_x)):
        if not IsPrime(int(str_x[i:])):
            return False
    return True

def all_left_truncatable_prime(tuple_x):
    list_prime = []
    for x in tuple_x:
        if IsTruncatablePrime(x):
            list_prime.append(x)
    return sorted(list_prime, reverse=True)