from math import sqrt

def all_right_truncatable_prime(t):
    x = t[11]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(k):
        if is_prime(k):
            l = str(k)
            for i in range(len(l) - 1):
                if not is_prime(int(l[:-i - 1])):
                    return False
            return True
        return False
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)