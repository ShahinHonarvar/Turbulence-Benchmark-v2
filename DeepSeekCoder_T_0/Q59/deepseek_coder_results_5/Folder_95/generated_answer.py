def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[77]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and left_truncatable_prime(i):
            result.append(i)
    return result