from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        if not i % 10 or i % 5 == 0:
            continue
        if is_prime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    break
                if not is_prime(int(str_i[:-j])):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)