def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(n ** 0.5) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

def left_trunc(n):
    while n != 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[3]
    ans = []
    for i in range(x, 0, -1):
        if is_prime(i) and left_trunc(i):
            ans.append(i)
    return ans