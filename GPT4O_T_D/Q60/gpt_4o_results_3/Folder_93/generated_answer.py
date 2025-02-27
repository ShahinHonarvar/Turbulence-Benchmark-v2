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

def left_right_truncatable(n):
    s = str(n)
    n_len = len(s)
    for i in range(n_len):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:n_len - i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[11]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and left_right_truncatable(i):
            result.append(i)
    return result