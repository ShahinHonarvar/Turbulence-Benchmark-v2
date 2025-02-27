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

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    while len(s) > 0:
        if not is_prime(int(s)) or not is_prime(int(s[::-1])):
            return False
        s = s[1:]
    return True

def all_left_right_truncatable_prime(t):
    if len(t) < 37:
        return []
    x = t[36]
    result = []
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)