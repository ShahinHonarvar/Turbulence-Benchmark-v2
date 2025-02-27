from math import sqrt

def all_left_truncatable_prime(t):
    x = t[88]
    result = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                is_left_truncatable = True
                for j in range(1, len(str_i)):
                    if not is_prime(int(str_i[j:])):
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    result.append(i)
    result.sort()
    return result