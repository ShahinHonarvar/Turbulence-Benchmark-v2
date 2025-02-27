def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == j:
                product = lst[i]
            else:
                product = lst[i]
                for k in range(i + 1, j):
                    product *= lst[k]
            if product == 40:
                result.append(lst[i:j])
    return result