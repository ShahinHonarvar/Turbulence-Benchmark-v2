import math

def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:i + 1])):
                return False
        return True
    result = []
    for n in x:
        if is_left_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)