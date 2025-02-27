from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    trial = 2
    sqrt_n = int(sqrt(n)) + 1
    while trial < sqrt_n:
        if n % trial == 0:
            return False
        trial += 1
    return True

def all_left_truncatable_prime(t):
    x = t[28]
    prime = []
    for i in range(2, x):
        if str(i) == str(i)[::-1] and is_prime(i):
            temp = i
            while temp != 0:
                if not is_prime(temp):
                    break
                if str(temp)[-1] == '0':
                    break
                temp = int(str(temp)[:-1])
            else:
                prime.append(i)
    return sorted(prime)