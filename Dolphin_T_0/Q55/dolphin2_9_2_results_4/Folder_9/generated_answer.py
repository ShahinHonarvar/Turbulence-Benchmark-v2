def lists_with_product_equal_n(lst):
    if not lst:
        return []

    def search(product_so_far, start_index, sublist):
        if product_so_far == -36 and len(sublist) > 0:
            result.append(sublist)
        for i in range(start_index, len(lst)):
            new_sublist = sublist + [lst[i]]
            search(product_so_far * lst[i], i + 1, new_sublist)
    result = []
    for i in range(len(lst)):
        search(lst[i], i + 1, [lst[i]])
    return result