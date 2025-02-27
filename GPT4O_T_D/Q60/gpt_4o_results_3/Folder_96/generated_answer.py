def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def is_right_truncatable_prime(n):
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[29]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    return result