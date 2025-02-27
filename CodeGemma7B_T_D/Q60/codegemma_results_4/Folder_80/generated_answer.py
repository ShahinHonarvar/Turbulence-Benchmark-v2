from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[14]
    ans = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            if '0' not in s and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
                ans.append(i)
    return sorted(ans, reverse=True)