def all_left_right_truncatable_prime(t):
    return [i for i in t if is_left_right_truncatable_prime(i)]

def is_left_right_truncatable_prime(n):
    if n <= 1 or n % 2 == 0:
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n) - 1):
        if not is_prime(int(str_n[i + 1:])):
            return False
    return is_prime(int(str_n[0]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True