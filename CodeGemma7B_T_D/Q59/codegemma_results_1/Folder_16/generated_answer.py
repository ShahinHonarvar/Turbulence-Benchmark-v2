def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[792]
    res = []
    for num in range(2, x):
        if is_prime(num) and left_truncatable_prime(num):
            res.append(num)
    return sorted(res)