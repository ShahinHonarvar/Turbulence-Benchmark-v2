from math import sqrt

def all_left_right_truncatable_prime(a):
    x = a[22]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    def right_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    result = []
    for n in range(x, 0, -1):
        if str(n).count('0') == 0 and is_prime(n) and left_truncatable_prime(n) and right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)