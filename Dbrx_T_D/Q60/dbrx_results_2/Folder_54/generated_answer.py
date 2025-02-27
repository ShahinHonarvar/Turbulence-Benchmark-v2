def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def truncate_left_right(n):
    while n > 9:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = tuple(range(2, t[88] + 1))
    return [i for i in x if is_prime(i) and truncate_left_right(i)][::-1]