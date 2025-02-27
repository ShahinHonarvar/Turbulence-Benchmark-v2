def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable(n):
    return all((is_prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)))

def all_left_right_truncatable_prime(t):
    x = t[81]
    return sorted([n for n in range(x, 1, -1) if left_right_truncatable(n)], reverse=True)