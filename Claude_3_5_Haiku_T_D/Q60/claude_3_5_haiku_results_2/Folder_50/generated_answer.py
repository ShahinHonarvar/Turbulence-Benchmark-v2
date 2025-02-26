def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    for i in range(1, len(num_str)):
        left = int(num_str[i:])
        right = int(num_str[:-i])
        if not is_prime(left) or not is_prime(right):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    result = []
    for num in range(x, 11, -1):
        if is_truncatable_prime(num):
            result.append(num)
    return result