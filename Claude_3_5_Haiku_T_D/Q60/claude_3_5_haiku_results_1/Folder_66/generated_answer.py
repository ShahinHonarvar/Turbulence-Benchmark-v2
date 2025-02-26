def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while len(str(n)) > 1:
        n_str = str(n)
        n = int(n_str[1:])
        if not is_prime(n):
            return False
    n_str = str(n)
    n = int(n_str[1:]) if len(n_str) > 1 else n
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[25]
    result = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result