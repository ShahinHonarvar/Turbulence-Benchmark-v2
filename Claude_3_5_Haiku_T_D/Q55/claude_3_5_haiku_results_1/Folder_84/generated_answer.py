def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                sublist.append(lst[current_index])
                product *= lst[current_index]
            if product == -906:
                result.append(sublist)
    return result