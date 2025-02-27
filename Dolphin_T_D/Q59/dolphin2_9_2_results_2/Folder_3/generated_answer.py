import math

def check_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[100]
    l = []
    for i in range(2, x):
        if check_prime(i):
            s = str(i)
            while len(s) > 1:
                if check_prime(int(s)):
                    s = s[1:]
                else:
                    break
            else:
                l.append(i)
    l.sort()
    return l