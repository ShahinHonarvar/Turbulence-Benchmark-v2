from math import sqrt

def all_right_truncatable_prime(lst):
    x = lst[71]
    result = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            k = len(str_i)
            for j in range(1, k):
                num = int(str_i[:-j])
                if not is_prime(num):
                    break
            else:
                result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True