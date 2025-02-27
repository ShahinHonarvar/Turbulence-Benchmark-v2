def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n in (2, 3) or n == 1:
        return True
    while n != 0:
        n, last = divmod(n, 10)
        if n != 0 and (not is_prime(n)):
            return False
        if n != 0 and last == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[80]
    l = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncanable_prime(i):
            l.append(i)
    l.sort(reverse=True)
    return l