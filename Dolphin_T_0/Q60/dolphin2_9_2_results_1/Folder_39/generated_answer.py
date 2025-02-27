def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_truncatable(n):
    while len(str(n)) > 1:
        n = int(str(n)[1:-1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[30]
    l = []
    for i in range(x, 0, -1):
        if check_truncatable(i):
            l.append(i)
    return l