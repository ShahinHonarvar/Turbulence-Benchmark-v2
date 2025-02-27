def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_right_truncatable_prime(n):
    a = []
    for x in range(2, n):
        if is_prime(x):
            for i in range(len(str(x)) - 1, 0, -1):
                if is_prime(int(str(x)[:i])):
                    if i == 1:
                        a.append(x)
        return sorted(a, reverse=True)