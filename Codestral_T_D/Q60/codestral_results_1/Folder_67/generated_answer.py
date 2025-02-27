def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    return is_prime(n) and all((is_prime(int(s[i:])) and is_prime(int(s[:-i])) for i in range(1, len(s))))

def all_left_right_truncatable_prime(n):
    x = n[70]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)], reverse=True)