def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    else:
        n_str = str(n)
        return is_prime(n) and n_str.count('0') == 0 and is_truncatable_prime(int(n_str[1:])) and is_truncatable_prime(int(n_str[:-1])) and is_truncatable_prime(int(n_str[1:-1]))

def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)], reverse=True)