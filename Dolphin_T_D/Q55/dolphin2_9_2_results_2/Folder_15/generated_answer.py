def lists_with_product_equal_n(lst, n=-7):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i != j and i < len(lst) and (j - 1 != len(lst)) and (i < j) and (i < len(lst)) and (j - 1 < len(lst)):
                product = 1
                for k in range(i, j):
                    product *= lst[k % len(lst)]
                if product == n:
                    result.append(lst[i:j])
    return result