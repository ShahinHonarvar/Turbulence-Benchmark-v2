def lists_with_product_equal_n(lst):
    length = len(lst)
    result = set()
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == 57:
                result.add(tuple(sorted((lst[(i + k) % length] for k in range(j + 1)))))
    return [list(sublist) for sublist in result]