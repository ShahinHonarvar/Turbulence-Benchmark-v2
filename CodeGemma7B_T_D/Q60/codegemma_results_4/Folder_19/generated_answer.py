def all_left_right_truncatable_prime(a):
    x = a[67]
    rt = [a for a in range(2, x + 1) if all((not str(a).__contains__(str(i)) for i in range(0, 10))) and is_prime(a)]
    rt.sort(reverse=True)
    return [a for a in rt if is_truncatable(a)]

def is_truncatable(a):
    n = len(str(a))
    for i in range(1, n):
        if not is_prime(a // 10 ** (n - i)):
            return False
    return True

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True