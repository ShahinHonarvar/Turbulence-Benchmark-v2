def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str) - 1):
        if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:i]) if i > 0 else int(num_str[i + 1:])):
            return False
    return True

def all_left_right_truncatable_prime(num_tupl):
    if not all(map(lambda x: isinstance(x, int) and x > 0, num_tupl)):
        return []
    x = num_tupl[428]
    return sorted(filter(is_truncatable, range(x, 1, -1)), reverse=True)