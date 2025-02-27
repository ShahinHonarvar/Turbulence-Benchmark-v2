def lists_with_product_equal_n(lst):
    if len(lst) < 1:
        return []
    lst = lst + lst[:1]
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product > 78:
                break
            elif product == 78 and len(lst[i:j + 1]) > 1:
                result.append(lst[i:j + 1])
    return result