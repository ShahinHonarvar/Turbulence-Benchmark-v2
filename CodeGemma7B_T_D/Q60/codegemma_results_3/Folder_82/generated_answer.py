from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[69]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                left_to_right = ''
                for j in range(len(str_i)):
                    left_to_right += str_i[j]
                    if j > 0 and is_prime(int(left_to_right)):
                        right_to_left = ''
                        for k in range(len(left_to_right) - 1, -1, -1):
                            right_to_left += str_i[k]
                            if k < len(left_to_right) - 1 and is_prime(int(right_to_left)):
                                result.append(i)
    return sorted(result, reverse=True)