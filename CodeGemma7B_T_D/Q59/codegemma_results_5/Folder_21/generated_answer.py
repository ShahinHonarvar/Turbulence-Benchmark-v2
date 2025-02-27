import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    result = []
    x = t[175]
    for i in range(2, x):
        if str(i).find('0') == -1 and is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                result.append(i)
    return sorted(result)