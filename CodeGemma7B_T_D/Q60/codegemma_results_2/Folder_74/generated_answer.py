from math import isprime

def all_left_right_truncatable_prime(t):
    x = t[36]
    result = []
    for i in range(2, x):
        str_i = str(i)
        if str_i.count('0') != 0 or isprime(i) != True:
            continue
        left = i
        right = i
        is_ok = True
        while left > 9:
            if isprime(left) != True:
                is_ok = False
                break
            str_left = str(left)
            left = int(str_left[1:])
        while right > 9:
            if isprime(right) != True:
                is_ok = False
                break
            str_right = str(right)
            right = int(str_right[:-1])
        if is_ok:
            result.append(i)
    result.sort()
    return result