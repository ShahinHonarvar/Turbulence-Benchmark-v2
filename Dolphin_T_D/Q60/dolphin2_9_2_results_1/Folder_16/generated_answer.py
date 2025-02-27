def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_lr_truncatable_prime(n):
    num_str = str(n)
    while len(num_str) > 1:
        if '0' in num_str:
            return False
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:-1]
    return is_prime(int(num_str)) if len(num_str) == 1 else is_prime(int(num_str[0] + num_str[-1]))

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[792]
    return sorted([int(num_str) for num_str in set((str(i) for i in range(2, x + 1))) if is_lr_truncatable_prime(int(num_str))])