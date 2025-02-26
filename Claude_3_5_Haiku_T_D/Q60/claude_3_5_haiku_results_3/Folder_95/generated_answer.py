def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[77]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        str_num = str(num)
        for left in range(len(str_num)):
            left_trunc = int(str_num[left:])
            if not is_prime(left_trunc):
                is_truncatable = False
                break
        for right in range(len(str_num)):
            right_trunc = int(str_num[:len(str_num) - right])
            if not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return sorted(result)