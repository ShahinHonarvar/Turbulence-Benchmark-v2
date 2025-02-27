def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == 76:
                result.append(lst[i:i + j + 1])
                if j != len(lst) - 1:
                    result.append(lst[i:i + j + 1] + lst[:i + j + 1 - len(lst)])
    return result