from math import sqrt

def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sqr = int(sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    n = t[73]
    p = []
    for i in range(n - 1, 1, -1):
        if '0' in str(i):
            continue
        cnt = len(str(i))
        flag = 1
        while cnt >= 0:
            if not is_prime(i):
                flag = 0
                break
            i = i % 10 ** cnt
            cnt -= 1
        if flag:
            p.append(i)
    return sorted(p, reverse=True)