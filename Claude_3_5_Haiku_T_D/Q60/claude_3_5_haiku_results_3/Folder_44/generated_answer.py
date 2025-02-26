def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[39]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        truncatable = True
        str_num = str(num)
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            if not is_prime(left_trunc):
                truncatable = False
                break
        if not truncatable:
            continue
        for i in range(len(str_num)):
            right_trunc = int(str_num[:len(str_num) - i])
            if not is_prime(right_trunc):
                truncatable = False
                break
        if truncatable and is_prime(num):
            result.append(num)
    return sorted(result)