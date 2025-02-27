import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[14]
    result = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        s = str(i)
        if '0' in s:
            continue
        for j in range(1, len(s)):
            if not is_prime(int(s[j:])) or not is_prime(int(s[:-j])):
                break
        else:
            result.append(i)
    result.sort(reverse=True)
    return result