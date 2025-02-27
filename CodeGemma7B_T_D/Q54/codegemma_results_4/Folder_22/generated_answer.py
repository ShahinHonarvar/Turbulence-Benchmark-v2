def all_right_truncatable_prime(tup):
    x = tup[84]
    tr = []
    for i in range(2, x):
        c = 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                c = 0
                break
        if c == 1:
            a = str(i)
            b = int(a[:-1])
            while b >= 2:
                c = 1
                for j in range(2, int(b ** 0.5) + 1):
                    if b % j == 0:
                        c = 0
                        break
                if c == 1:
                    tr.append(i)
                b = int(str(b)[:-1])
    return sorted(tr)