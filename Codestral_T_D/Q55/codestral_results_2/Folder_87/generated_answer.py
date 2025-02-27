def lists_with_product_equal_n(lst):
    n = 27
    if not lst:
        return []
    len_lst = len(lst)
    lst *= 2
    result = []
    for start in range(len_lst):
        for end in range(start + 1, 2 * len_lst):
            sublist = lst[start:end]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result