def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result

def is_left_right_truncatable_prime(num):
    if num < 2:
        return False
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    left = str(num)
    right = str(num)
    while len(left) > 1:
        left = left[1:]
        right = right[:-1]
        if not (is_prime(int(left)) and is_prime(int(right))):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True