import math

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i + 1:])):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return result