def lists_with_product_equal_n(lst):

    def gcd(a, b):
        return b if a == 0 else gcd(b % a, a)
    n = len(lst)
    prods = [0] * n
    pwd = [0] * n
    pwd[n - 1] = lst[n - 1]
    prods[n - 1] = lst[n - 1]
    for i in range(n - 2, -1, -1):
        pwd[i] = pwd[i + 1] * lst[i]
        prods[i] = gcd(pwd[i], lst[i])
    res = []
    for j in range(n):
        for k in range(j + 1, n):
            if pwd[j] * prods[k] != -6:
                continue
            product = pwd[j]
            for l in range(j + 1, k):
                product *= lst[l]
            if product == -6:
                res.append(lst[j:k + 1])
    return res