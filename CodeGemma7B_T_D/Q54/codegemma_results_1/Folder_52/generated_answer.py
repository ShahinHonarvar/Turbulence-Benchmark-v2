def all_right_truncatable_prime(s):
    prima = s[52]
    c = list(range(2, prima))
    f = True
    d = []
    n = 0
    while n != prima:
        n = c[n]
        for i in range(1, prima):
            x = n
            for j in range(i):
                x //= 10
            for k in range(x, 0, -1):
                if k == 2 or k == 3 or k == 5 or (k == 7):
                    continue
                if n % k == 0:
                    f = False
                    break
            if f:
                d.append(n)
        for i in range(n, len(c)):
            c[i] += n
        n += 1
        f = True
    d.sort(reverse=True)
    return d