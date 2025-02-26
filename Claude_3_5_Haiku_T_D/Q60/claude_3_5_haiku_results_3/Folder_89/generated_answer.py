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
        left_truncate = int(str(n)[len(str(n)) - i:])
        right_truncate = int(str(n)[:i])
        while len(str(left_truncate)) > 0 and len(str(right_truncate)) > 0:
            if not is_prime(left_truncate) or not is_prime(right_truncate):
                return False
            left_truncate = int(str(left_truncate)[1:]) if len(str(left_truncate)) > 1 else 0
            right_truncate = int(str(right_truncate)[:-1]) if len(str(right_truncate)) > 1 else 0
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[97]
    result = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result