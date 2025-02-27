def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i != j - 1:
                product = 1
                if j != len(lst) + 1:
                    for k in range(i, j):
                        product *= lst[k % len(lst)]
                    if product == -18:
                        result.append(lst[i:j])
    return result