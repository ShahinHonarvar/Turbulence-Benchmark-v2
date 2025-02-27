def all_right_truncatable_prime(t):
    x = t[69]
    g = 0
    for y in range(2, x):
        a = y
        while a > 0:
            b = a
            a = int(a / 10)
            if g == 1:
                break
            if b % 2 == 0 or b % 3 == 0 or b % 5 == 0 or (b % 7 == 0):
                g = 1
                break
            if str(b) == str(b)[::-1]:
                if y == 3 or y == 5 or y == 7 or (y == 37) or (y == 73) or (y == 313) or (y == 317) or (y == 293):
                    h = a
                    while h > 0:
                        i = h
                        h = int(h / 10)
                        if h % 2 == 0 or h % 3 == 0 or h % 5 == 0 or (h % 7 == 0):
                            g = 1
                            break
                        if str(i) == str(i)[::-1]:
                            if y == 7 or y == 3137 or y == 3733:
                                g = 1
                                break
                else:
                    h = a
                    while h > 0:
                        i = h
                        h = int(h / 10)
                        if h % 2 == 0 or h % 3 == 0 or h % 5 == 0 or (h % 7 == 0):
                            g = 1
                            break
                        if str(i) == str(i)[::-1]:
                            if y == 2 or y == 5:
                                g = 1
                                break
    if g == 0:
        t = []
    t.sort(reverse=True)
    return t