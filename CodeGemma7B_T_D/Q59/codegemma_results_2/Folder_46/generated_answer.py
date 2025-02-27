import math

def all_left_truncatable_prime(a):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(a[33]):
        if is_prime(i) and (not str(i).startswith('0')) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
            result.append(i)
    return sorted(result)