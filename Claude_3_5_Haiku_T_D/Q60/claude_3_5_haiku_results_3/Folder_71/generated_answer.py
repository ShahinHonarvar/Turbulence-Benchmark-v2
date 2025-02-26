def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[22]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        str_num = str(num)
        for length in range(len(str_num), 0, -1):
            left_trunc = int(str_num[:length])
            right_trunc = int(str_num[-length:])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return result