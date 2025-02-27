def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if '0' in str(n):
        return False
    n_str = str(n)
    for i in range(len(n_str) - 1, 0, -1):
        if not is_prime(int(n_str[i:])):
            return False
    return True

def all_left_truncatable_prime(y):
    x = y[70]
    prime_list = [i for i in range(x - 1, 0, -1) if is_prime(i) and is_truncatable(i)]
    return prime_list