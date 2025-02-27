def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def is_truncatable(n):
    return all((int(str(n)[i:j]) != 0 and is_prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)))

def all_left_right_truncatable_prime(t):
    x = t[42]
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)])