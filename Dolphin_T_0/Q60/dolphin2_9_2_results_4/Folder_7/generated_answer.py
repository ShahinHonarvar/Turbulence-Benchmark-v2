def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            if is_prime(num):
                for i in range(len(str_num)):
                    if len(str_num) - i > 1:
                        if is_prime(num // 10 ** i % 10 ** (len(str_num) - 2 * i - 1)):
                            continue
                    else:
                        break
                else:
                    result.append(num)
    return result