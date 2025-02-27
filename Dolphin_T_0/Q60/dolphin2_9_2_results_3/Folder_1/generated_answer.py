def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

def is_truncatable(n, left, right):
    if n // 10 ** left != n // 10 ** (left + 1) and n // 10 ** right != n % 10 ** right and is_prime(n // 10 ** left) and is_prime(n % 10 ** (right + 1)):
        return True
    else:
        return False

def all_left_right_truncatable_prime(t):
    x = t[20]
    truncatable_list = [i for i in range(2, x + 1) if is_truncatable(i, 1, 1)]
    truncatable_list.sort(reverse=True)
    return truncatable_list