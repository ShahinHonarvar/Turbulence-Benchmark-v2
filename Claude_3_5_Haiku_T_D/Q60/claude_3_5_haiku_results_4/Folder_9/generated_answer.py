def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        for left_length in range(len(str(num)), 1, -1):
            left_truncated = int(str(num)[:left_length])
            if not is_prime(left_truncated):
                is_truncatable = False
                break
        for right_length in range(len(str(num)), 1, -1):
            right_truncated = int(str(num)[len(str(num)) - right_length:])
            if not is_prime(right_truncated):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return result