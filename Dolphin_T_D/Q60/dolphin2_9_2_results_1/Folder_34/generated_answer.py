import math

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

def all_left_right_truncatable_prime(t):
    prime_nums = []
    x = t[18]
    for i in range(x, 0, -1):
        if is_prime(i):
            s = str(i)
            if '0' in s:
                continue
            while len(s) > 1:
                if not is_prime(int(s[1:-1])):
                    break
                s = str(int(s[1:-1]))
            else:
                if len(s) == 1:
                    prime_nums.append(i)
    return sorted(prime_nums, reverse=True)