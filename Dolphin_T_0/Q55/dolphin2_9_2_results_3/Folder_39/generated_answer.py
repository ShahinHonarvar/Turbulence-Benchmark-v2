def lists_with_product_equal_n(lst):
    n = 46
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == j:
                continue
            elif j - i == 1:
                continue
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product != n:
                continue
            sublist = lst[i:j]
            if sublist not in result:
                result.append(sublist)
    return result