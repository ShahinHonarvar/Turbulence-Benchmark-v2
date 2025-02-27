def all_right_truncatable_prime(t):
    x = t[54]
    r = []
    d = [2, 3, 5, 7]
    f = [10 ** i for i in range(1, 6)][::-1]
    for i in d:
        if i < x:
            r += [i]
    for i in f:
        for j in d:
            if i * j < x:
                r += [i * j]
    r = list(filter(lambda n: all(map(lambda x: n % x, d)), r))
    while len(r) > 0:
        n = r.pop()
        if all(map(lambda x: n % x, d)):
            s = str(n)
            while len(s) > 0:
                s = s[:-1]
                if int(s) in r:
                    for j in s:
                        if int(s) < x:
                            r += [int(s)]
            else:
                return []
    return list(sorted(r, reverse=True))