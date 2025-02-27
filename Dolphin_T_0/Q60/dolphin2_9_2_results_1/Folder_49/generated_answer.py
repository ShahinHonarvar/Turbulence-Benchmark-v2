def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate(n):
    return [int(str(n)[i:j]) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)]

def all_left_right_truncatable_prime(t):
    x = t[14]
    return sorted([n for n in range(2, x + 1) if is_prime(n) and all((is_prime(m) for m in truncate(n)))])