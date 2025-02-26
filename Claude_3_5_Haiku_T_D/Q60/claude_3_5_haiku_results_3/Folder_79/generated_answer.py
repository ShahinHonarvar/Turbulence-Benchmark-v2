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
    temp_num = num
    while temp_num > 9:
        temp_num //= 10
        if not is_prime(temp_num):
            return False
    full_str = str(num)
    while len(full_str) > 1:
        full_str = full_str[1:]
        if not is_prime(int(full_str)):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[91]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)