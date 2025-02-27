def product(l, n):
    if n == 1:
        product = 1
        for i in l:
            product *= i
        return product
    else:
        return product(l[:-1], n - 1) * l[-1]

def lists_with_product_equal_n(l):
    list_sublist = []
    for n in range(len(l)):
        for m in range(n, len(l)):
            if product(l[n:m + 1], m - n + 1) == -8:
                list_sublist.append(list(l[n:m + 1]))
    return list_sublist