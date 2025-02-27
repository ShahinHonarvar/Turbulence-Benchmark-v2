def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    property_list = []
    for i in range(n):
        product = 1
        for j in range(i, n * 2):
            product *= lst[j % n]
            if product == -41:
                property_list.append(lst[i:j % n + 1])
    return property_list