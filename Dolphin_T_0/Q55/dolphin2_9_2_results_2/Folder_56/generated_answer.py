def lists_with_product_equal_n(lst):
    result = []
    total_product = 1
    product_set = set()
    for i in range(len(lst)):
        total_product *= lst[i]
        if total_product == -65:
            product_set.add(tuple(lst[:i + 1]))
    for i in range(1, len(lst)):
        total_product = total_product // lst[i - 1]
        if total_product == -65:
            product_set.add(tuple(lst[i:]))
    for subset in product_set:
        result.append(list(subset))
    return result