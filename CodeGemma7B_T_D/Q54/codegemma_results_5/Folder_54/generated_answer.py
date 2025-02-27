from math import sqrt

def all_right_truncatable_prime(a):
    a = a[88]
    l = []
    for i in range(2, a):
        c = 0
        b = i
        k = int(sqrt(b))
        for j in range(2, k + 1):
            if b % j == 0:
                c = 1
                break
        if c == 0:
            b /= 10
            while b > 0:
                c = 0
                k = int(sqrt(b))
                for j in range(2, k + 1):
                    if b % j == 0:
                        c = 1
                        break
                if c == 0:
                    l.append(i)
                    break
                else:
                    b /= 10
    l.sort(reverse=True)
    return l