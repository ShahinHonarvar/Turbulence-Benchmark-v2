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

def truncate_right(n):
    while n > 9:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(t):
    x = tuple(t)[126]
    return sorted([i for i in range(2, x) if truncate_right(i)], reverse=True) if x > 2 else []