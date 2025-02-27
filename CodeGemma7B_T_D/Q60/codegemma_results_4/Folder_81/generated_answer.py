from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[98]
    result = []
    for num in range(2, x + 1):
        if str(num).find('0') == -1 and is_prime(num):
            temp = str(num)
            while len(temp) > 1:
                if not is_prime(int(temp)):
                    break
                temp = temp[1:]
            if len(temp) == 1 and is_prime(int(temp)):
                result.append(num)
    return sorted(result)