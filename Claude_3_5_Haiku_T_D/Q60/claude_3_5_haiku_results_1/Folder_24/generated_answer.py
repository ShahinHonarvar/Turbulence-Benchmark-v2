def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[65]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num):
                is_truncatable = False
                break
        temp_num = num
        while temp_num > 9:
            temp_num %= 10 ** (len(str(temp_num)) - 1)
            if not is_prime(temp_num):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return result