def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    if lst_len < 1:
        return []
    index_1 = 0
    index_2 = 0
    result = []
    while index_2 < lst_len:
        if index_1 > index_2:
            index_1 = index_2
        product = 1
        for i in range(index_1, index_2 + 1):
            product *= lst[i]
        if product == -95:
            curr_indices = [i for i in range(index_1, index_2 + 1)]
            if curr_indices not in result:
                result.append(curr_indices)
        if index_2 == lst_len - 1:
            index_1 += 1
            index_2 = index_1 + 1
        else:
            index_2 += 1
    return result