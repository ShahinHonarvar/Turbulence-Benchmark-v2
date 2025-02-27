def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, i=0):
    if i > len(str(n)) - 1:
        return True
    if is_prime(int(str(n)[i:] + str(n)[:i])) and is_prime(int(str(n)[i:] + str(n)[i + 1:])):
        return is_truncatable(n, i + 1)
    return False

def all_left_right_truncatable_prime(t):
    x = t[25]
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)], reverse=True) or []