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

def right_truncatable(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[65]
    ret = []
    for num in range(x - 1, 0, -1):
        if right_truncatable(num) and is_prime(num):
            ret.append(num)
    return ret