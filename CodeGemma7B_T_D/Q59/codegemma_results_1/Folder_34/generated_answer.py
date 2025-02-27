from math import sqrt

def all_left_truncatable_prime(args):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:i])):
                return False
        return True
    result = []
    for arg in args:
        if left_truncatable_prime(arg) and arg < args[18]:
            result.append(arg)
    result.sort(reverse=True)
    return result