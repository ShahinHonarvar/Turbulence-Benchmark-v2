import math

def all_right_truncatable_prime(t):

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    x = t[92]
    result = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[:-j])):
                    break
            else:
                result.append(i)
    result.sort()
    return result