def all_right_truncatable_prime(t):
    x = t[86]
    factors = [2, 3, 5, 7, 11]
    l = []
    for i in range(2, x):
        for j in factors:
            if i % j == 0:
                break
        else:
            n = i
            str_n = str(n)
            while True:
                if len(str_n) <= 1:
                    break
                n = int(str_n[:-1])
                for j in factors:
                    if n % j == 0:
                        break
                else:
                    l.append(i)
                str_n = str(n)
    l.sort(reverse=True)
    return l