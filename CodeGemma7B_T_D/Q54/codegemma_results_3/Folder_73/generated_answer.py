from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[97]
    result = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            for i in reversed(range(1, len(str_num))):
                truncated_num = int(str_num[:i])
                if not is_prime(truncated_num):
                    break
            else:
                result.append(num)
    return sorted(result)