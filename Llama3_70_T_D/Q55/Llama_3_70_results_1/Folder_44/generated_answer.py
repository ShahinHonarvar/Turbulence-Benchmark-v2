def lists_with_product_equal_n(lst):
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = lst[i:i + size]
            if len(sublist) < size:
                sublist += lst[:size - len(sublist)]
            if 0 in sublist:
                continue
            product = 1
            for j in sublist:
                product *= j
            if product == 29:
                result.append(sublist)
    return result