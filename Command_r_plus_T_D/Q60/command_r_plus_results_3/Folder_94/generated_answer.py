def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        left_trunc = num_str[i:]
        if not is_prime(int(left_trunc)) or '0' in left_trunc:
            return False
    for i in range(len(num_str) - 1, -1, -1):
        right_trunc = num_str[:i]
        if not is_prime(int(right_trunc)) or '0' in right_trunc:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    result = []
    for num in range(start, end + 1):
        if left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)