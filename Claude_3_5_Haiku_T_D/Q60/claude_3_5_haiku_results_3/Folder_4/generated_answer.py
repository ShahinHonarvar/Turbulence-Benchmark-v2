def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n)), 0, -1):
        left = str(n)[:i]
        right = str(n)[-i:]
        if not (is_prime(int(left)) and is_prime(int(right))):
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[96]
    result = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result