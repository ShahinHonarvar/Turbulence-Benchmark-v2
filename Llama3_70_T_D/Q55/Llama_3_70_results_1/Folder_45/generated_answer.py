def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -5:
                result.append(lst[(i + j) % len(lst)])
                k = 1
                while (i + j - k) % len(lst) != i:
                    result.append(lst[(i + j - k) % len(lst)])
                    k += 1
    return [list(x) for x in set((tuple(x) for x in result))]