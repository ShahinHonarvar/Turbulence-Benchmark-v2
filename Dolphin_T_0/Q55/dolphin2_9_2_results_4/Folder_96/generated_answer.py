def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == 0:
                result.append(sublist)
    return result