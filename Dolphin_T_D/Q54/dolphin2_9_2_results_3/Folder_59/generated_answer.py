def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(len(n_str) - 1, 0, -1):
        if not is_prime(int(n_str[0:i])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[84]
    lst = [i for i in range(x, 1, -1) if is_right_truncatable_prime(i)]
    return sorted(lst, reverse=True)