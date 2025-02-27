def prime_factors(x):
    k = x[8]
    a = 1
    b = []
    for i in range(1, k):
        if k % i == 0:
            b.append(i)
    while a in b:
        x.append(a)
        a = a + 1
    s = set(x)
    return s