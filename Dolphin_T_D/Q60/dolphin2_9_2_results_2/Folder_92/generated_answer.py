def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[7]
    res = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num and is_prime(num):
            for i in range(len(str_num) - 1):
                if len(str_num) - i - 1 >= 1 and i + 1 >= 1:
                    left_trunc = int(str_num[i + 1:])
                    right_trunc = int(str_num[:i + 1])
                    if is_prime(left_trunc) and is_prime(right_trunc):
                        res.append(num)
    return sorted(res)