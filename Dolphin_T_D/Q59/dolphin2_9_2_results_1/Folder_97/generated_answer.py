def is_prime(n):
    if n <= 1:
        return None
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[645]
    return sorted([i for i in range(10, x) if is_prime(i) and is_prime(int(str(i)[1:]))])