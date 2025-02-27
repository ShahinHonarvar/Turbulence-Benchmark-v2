def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    lst = lst + lst[:-1]
    result = []
    product = 1
    for i in range(n):
        product *= lst[i]
        if product == -906:
            all_sublists = [lst[i + 1:j + 1] for j in range(i + 1, n + i + 1)]
            result.extend(all_sublists)
    return result