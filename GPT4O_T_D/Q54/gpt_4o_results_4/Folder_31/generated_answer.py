def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num > 0:
        num //= 10
        if num > 0 and (not is_prime(num)):
            return False
    return True

def all_right_truncatable_prime(tpl):
    if len(tpl) > 50:
        x = tpl[50]
        result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
        return sorted(result, reverse=True)
    return []