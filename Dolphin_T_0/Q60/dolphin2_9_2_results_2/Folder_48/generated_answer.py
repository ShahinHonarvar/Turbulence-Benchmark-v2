import math

def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_n = n
        while n > 9:
            n = n // 10
            if not is_prime(n):
                return False
        n = n_n
        while n > 9:
            n = int(str(n).rstrip('0').rstrip('1'))
            if not is_prime(n):
                return False
        return True
    result = [2] if x >= 2 else []
    for i in range(3, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return result