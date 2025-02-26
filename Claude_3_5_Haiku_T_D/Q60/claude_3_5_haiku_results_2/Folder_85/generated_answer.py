def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[94]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_truncatable = False
                    break
                temp_num //= 10
            if is_truncatable:
                temp_num = num
                str_num = str(temp_num)
                while len(str_num) > 0:
                    if not is_prime(int(str_num)):
                        is_truncatable = False
                        break
                    str_num = str_num[1:]
                if is_truncatable:
                    result.append(num)
    return sorted(result)