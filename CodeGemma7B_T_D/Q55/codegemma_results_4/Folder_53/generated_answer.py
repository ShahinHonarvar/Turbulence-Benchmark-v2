def lists_with_product_equal_n(lst):
    for i in range(len(lst)):
        prod = lst[i]
        for j in range(i + 1, len(lst)):
            prod *= lst[j]
            if prod == -87:
                return [[lst[i], lst[j]]]
    return []