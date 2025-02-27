from math import sqrt

def all_left_truncatable_prime(tp):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    x = tp[70]
    res = []
    for i in range(2, x):
        if str(i) not in '0' and all_prime(i):
            c = i
            temp = ''
            while c > 0:
                temp = str(c % 10) + temp
                if c <= 9:
                    break
                c //= 10
            if all_prime(int(temp)):
                res.append(i)
    return sorted(res, reverse=True)