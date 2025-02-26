def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[97]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:]
            if not is_prime(int(str_num)):
                left_right_truncatable = False
                break
        str_num = str(num)
        while len(str_num) > 1 and left_right_truncatable:
            str_num = str_num[:-1]
            if not is_prime(int(str_num)):
                left_right_truncatable = False
                break
        if left_right_truncatable and is_prime(num):
            result.append(num)
    return sorted(result)