def all_right_truncatable_prime(n):
    x = n[41]
    a = list(range(2, x))
    b = []
    for i in range(len(a)):
        if is_prime(a[i]) and is_truncatable(a[i]):
            b.append(a[i])
    b.sort(reverse=True)
    return b

def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def is_truncatable(a):
    while a != 0:
        if not is_prime(a):
            return False
        a = a // 10
    return True