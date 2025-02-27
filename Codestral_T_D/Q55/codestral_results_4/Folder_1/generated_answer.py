def lists_with_product_equal_n(lst):
    n = -51
    double_lst = lst + lst
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            prod = 1
            for k in range(i, j):
                prod *= double_lst[k]
                if prod == n:
                    result.append(double_lst[i:k + 1])
    return result