def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    left_truncatable = True
    right_truncatable = True
    for i in range(len(str(num))):
        left_truncated = int(str(num)[i:])
        right_truncated = int(str(num)[:len(str(num)) - i])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False
    return left_truncatable and right_truncatable

def all_left_right_truncatable_prime(tuple_input):
    x = tuple_input[55]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result)