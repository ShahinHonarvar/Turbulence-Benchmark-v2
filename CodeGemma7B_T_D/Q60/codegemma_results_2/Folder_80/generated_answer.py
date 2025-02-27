from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(lst):
    result = []
    for i in lst:
        str_i = str(i)
        if '0' in str_i:
            continue
        for j in range(1, len(str_i)):
            if is_prime(int(str_i[j:])):
                result.append(int(str_i))
                break
    return result

def right_truncatable_prime(lst):
    result = []
    for i in lst:
        str_i = str(i)
        if '0' in str_i:
            continue
        for j in range(len(str_i) - 1):
            if is_prime(int(str_i[:j + 1][::-1])):
                result.append(int(str_i))
                break
    return result

def all_left_right_truncatable_prime(tup):
    x = tup[14]
    lst = range(3, x + 1)
    left_trun = left_truncatable_prime(lst)
    right_trun = right_truncatable_prime(lst)
    result = []
    for i in left_trun:
        if i in right_trun:
            result.append(i)
    result.sort(reverse=True)
    return result or []