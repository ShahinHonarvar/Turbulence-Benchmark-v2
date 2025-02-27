from math import sqrt
    from itertools import count

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for divisor in range(2, int(sqrt(n)) + 1):
            if n % divisor == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i:])):
                return False
        return True
    result = []
    for num in count(2):
        if num > x:
            break
        if is_prime(num) and is_truncatable(num):
            result.append(num)
    return result