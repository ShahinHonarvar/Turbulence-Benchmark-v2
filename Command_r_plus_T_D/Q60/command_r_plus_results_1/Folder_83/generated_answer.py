def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[:i])) or not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    result = []
    for num in range(start, end + 1):
        if num < 10:
            continue
        if str(num).count('0') > 0:
            continue
        if left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)