def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product == 29:
                    result.append(lst[i:k + 1])
                elif product > 29:
                    break
    return result