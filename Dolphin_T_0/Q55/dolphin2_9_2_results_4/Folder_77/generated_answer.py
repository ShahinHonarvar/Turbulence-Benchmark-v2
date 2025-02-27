def product(sublist):
    res = 1
    for x in sublist:
        res *= x
    return res

def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = lst[i:j]
            if product(sublist) == 632 or product(sublist[::-1]) == 632:
                res.append(list(sublist))
    return res