from sympy import isprime

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not isprime(int(str_num[i:])):
            continue
        for j in range(len(str_num) - 1):
            if not isprime(int(str_num[i:len(str_num) - j])):
                break
        else:
            return True
    return False

def all_left_right_truncatable_prime(num):
    result = []
    for i in range(2, num + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)