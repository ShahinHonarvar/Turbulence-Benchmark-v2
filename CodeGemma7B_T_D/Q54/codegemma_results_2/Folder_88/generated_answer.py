import math

def all_right_truncatable_prime(n):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for num in n:
        if is_prime(num):
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:-i])):
                    break
            else:
                result.append(num)
    result.sort()
    return result