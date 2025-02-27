def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[645]
    result = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            new_num = int(str_num[i:])
            if not is_prime(new_num):
                is_truncatable = False
                break
            new_num = int(str_num[:len(str_num) - i])
            if not is_prime(new_num):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return result