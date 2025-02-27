def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    m = int(n ** 0.5) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

def left_truncatable(n):
    if n <= 0:
        return False
    num = n
    while num != 0:
        num = num // 10
        if not is_prime(num):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[4]
    res = [i for i in range(x) if is_prime(i) and left_truncatable(i)]
    return sorted(res)