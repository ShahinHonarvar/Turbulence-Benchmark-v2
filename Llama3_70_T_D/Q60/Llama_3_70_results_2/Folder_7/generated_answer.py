def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    digits = str(n)
    if '0' in digits:
        return False
    for i in range(1, len(digits)):
        if not is_prime(int(digits[i:])) or not is_prime(int(digits[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    return sorted((i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)))