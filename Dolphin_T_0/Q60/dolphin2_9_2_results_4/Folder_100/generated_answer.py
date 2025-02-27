import math

def all_left_right_truncatable_prime(t):

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

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n) - 1):
            if not is_prime(int(str_n[i + 1:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    res = []
    x = t[26]
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            res.append(i)
    return res