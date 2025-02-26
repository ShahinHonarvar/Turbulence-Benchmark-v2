def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    digits = str(num)
    while len(digits) > 0:
        current = int(digits)
        if not is_prime(current):
            return False
        digits = digits[1:]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    result = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result