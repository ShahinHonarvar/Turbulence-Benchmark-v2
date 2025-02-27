import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p = p + 2
    return True

def all_right_truncatable_prime(x):
    prime = []
    for i in range(x, 1, -1):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j = j // 10
            if j == 0:
                prime.append(i)
    return sorted(prime, reverse=True)