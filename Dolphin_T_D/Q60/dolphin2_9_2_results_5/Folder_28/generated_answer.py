def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    if str(n)[0] == '0' or str(n)[-1] == '0':
        return False
    return all((is_prime(int(str(n)[1:-1])) and is_prime(int(str(n)[:-1])) for _ in range(1, len(str(n)) - 1)))

def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)])