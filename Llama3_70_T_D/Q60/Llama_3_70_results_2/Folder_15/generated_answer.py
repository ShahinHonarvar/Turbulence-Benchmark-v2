def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
        if not is_prime(int(n_str[:-i - 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable(i)], reverse=True)