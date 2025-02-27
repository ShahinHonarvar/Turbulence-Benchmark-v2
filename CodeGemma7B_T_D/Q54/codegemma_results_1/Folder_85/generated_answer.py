import math
    from primePy import primality

def all_right_truncatable_prime(a):

    def is_prime(num):
        if num % 2 == 0:
            return False
        i = 3
        while i <= int(math.sqrt(num)):
            if num % i == 0:
                return False
            i += 2
        return True

    def remove_rightmost_digit(num):
        str_num = str(num)
        str_num = str_num[:-1]
        return int(str_num)
    x = a[94]
    result = []
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = remove_rightmost_digit(temp)
            else:
                result.append(i)
    return sorted(result)