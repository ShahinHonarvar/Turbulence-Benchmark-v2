def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if n < 10:
        return n != 0 and n != 1
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:i])) or n_str[i:].startswith('0') or n_str[:i].startswith('0'):
            return False
    return True

def all_left_right_truncatable_prime(x):
    prime_list = [i for i in range(2, x + 1) if is_prime(i)]
    return sorted([i for i in prime_list if is_truncatable(i)], reverse=True)