from math import sqrt

def all_right_truncatable_prime(a):

    def is_prime(a):
        if a <= 1:
            return False
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

    def right_truncatable_prime(a):
        for i in range(1, len(str(a))):
            if not is_prime(int(str(a)[:-i])):
                return False
        return True
    x = a[41]
    result = []
    for i in range(2, x):
        if is_prime(i) and right_truncatable_prime(i):
            result.append(i)
    return sorted(result)