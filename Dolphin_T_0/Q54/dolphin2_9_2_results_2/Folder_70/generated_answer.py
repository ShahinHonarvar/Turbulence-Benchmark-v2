def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable(n):
    if len(str(n)) <= 1:
        return True
    return is_prime(n) and is_right_truncatable(int(str(n)[-1]))

def all_right_truncatable_prime(l: tuple):
    x = l[433]
    lst = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(lst, reverse=True) or []