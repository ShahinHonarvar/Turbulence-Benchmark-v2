def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[1:]) if len(str(num)) > 1 else 0
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)