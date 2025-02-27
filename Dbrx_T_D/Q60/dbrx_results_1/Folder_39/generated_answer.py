from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[30]
    result = []
    for num in range(2, x + 1):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_lr_truncatable = True
                for i in range(1, len(str_num)):
                    if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
                        is_lr_truncatable = False
                        break
                if is_lr_truncatable:
                    result.append(num)
    return sorted(result, reverse=True)