from math import sqrt

def all_left_truncatable_prime(x):

    def prime(x):
        if x <= 1:
            return False
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def left_truncatable_prime(x):
        if '0' in str(x):
            return False
        s = str(x)
        for i in range(1, len(s)):
            if not prime(int(s[i:])):
                return False
        return True

    def all_left_truncatable_prime(x):
        return sorted([i for i in range(x) if left_truncatable_prime(i)], reverse=True)