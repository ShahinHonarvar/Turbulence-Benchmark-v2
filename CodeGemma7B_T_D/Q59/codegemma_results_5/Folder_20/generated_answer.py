import math

def all_left_truncatable_prime(num):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    result = []
    for i in range(2, num):
        if is_left_truncatable(i):
            result.append(i)
    result.sort(reverse=True)
    return result