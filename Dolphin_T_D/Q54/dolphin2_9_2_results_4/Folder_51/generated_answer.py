import math

def all_right_truncatable_prime(n):

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def is_truncatable(x):
        s = str(x)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = n[54]
    return sorted([i for i in range(n[54]) if is_truncatable(i) and is_prime(i)])