import math

def all_right_truncatable_prime(x):

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    result = []
    for num in x:
        str_num = str(num)
        for i in range(1, len(str_num)):
            truncated_num = int(str_num[:-i])
            if is_prime(truncated_num):
                result.append(truncated_num)
    return sorted(result)