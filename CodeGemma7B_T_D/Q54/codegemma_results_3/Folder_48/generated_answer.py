def all_right_truncatable_prime(tp):
    x = tp[835]
    rprime = []
    for i in range(2, x):
        tmp = i
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i1 = 0
        for j in range(10, x):
            if i % j == 0:
                a = 1
                break
            if i % (j + 1) == 0:
                b = 1
                break
            if i % (j + 2) == 0:
                c = 1
                break
            if i % (j + 3) == 0:
                d = 1
                break
            if i % (j + 4) == 0:
                e = 1
                break
            if i % (j + 5) == 0:
                f = 1
                break
            if i % (j + 6) == 0:
                g = 1
                break
            if i % (j + 7) == 0:
                h = 1
                break
            if i % (j + 8) == 0:
                i1 = 1
                break
        if a != 1 and b != 1 and (c != 1) and (d != 1) and (e != 1) and (f != 1) and (g != 1) and (h != 1) and (i1 != 1):
            while tmp >= 1:
                tmp = int(tmp / 10)
                if tmp == 0:
                    break
                if tmp >= 2:
                    for j in range(2, tmp):
                        if tmp % j == 0:
                            break
                    if tmp % j != 0:
                        rprime.append(i)
                        break
                tmp = int(tmp / 10)
    if rprime != []:
        return sorted(rprime)
    else:
        return rprime