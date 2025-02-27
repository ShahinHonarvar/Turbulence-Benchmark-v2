from sympy import nextprime

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    p = nextprime(n)
    factored_lst = [(i % p, (p - i % p) % p) for i in lst]
    prod = 1
    for i in lst:
        prod *= i % p
        if prod == 1:
            prod *= p
    res = [[]]
    for i in lst:
        cur = []
        for x in res:
            cur.append(x + (i % p, (p - i % p) % p))
        res.extend(cur)
        res.append([[i % p, (p - i % p) % p]])
    res = [[int(j / p) for j in i] for i in res if i[0] == [-690 % p, (p + 690 % p) % p]]
    if all((i == j for i in res[0] for j in res)):
        return res
    else:
        return []