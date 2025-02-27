import math

def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    for i in reversed(range(2, x)):
        if is_prime(i):
            flag = True
            for j in str(i):
                if j == '0':
                    flag = False
                    break
            if flag:
                t = i
                while t > 0:
                    if not is_prime(t):
                        flag = False
                        break
                    t //= 10
                if flag:
                    res.append(i)
    return sorted(res, reverse=True)