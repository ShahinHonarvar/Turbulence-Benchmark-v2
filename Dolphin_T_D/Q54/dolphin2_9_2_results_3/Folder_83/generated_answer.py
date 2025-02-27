def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    return True

def all_right_truncatable_prime(x):
    result_list = []
    for n in range(2, x):
        if is_prime(n) and is_truncatable(n):
            result_list.append(n)
    return sorted(result_list)