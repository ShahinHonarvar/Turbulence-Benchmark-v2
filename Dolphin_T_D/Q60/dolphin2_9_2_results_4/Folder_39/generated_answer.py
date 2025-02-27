import math

def is_left_and_right_truncatable_prime(n):
    while True:
        if not is_prime(n):
            return False
        n_digits = [int(it) for it in str(n)]
        if 0 in n_digits:
            return False
        if len(n_digits) == 1:
            return True
        if is_prime(int(''.join(map(str, n_digits[:-1])))) and is_prime(int(''.join(map(str, n_digits[1:])))):
            n = int(''.join(map(str, n_digits[1:-1])))
        else:
            break
    return True

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for it in range(2, int(math.sqrt(n)) + 1):
        if n % it == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[30]
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)], reverse=True)