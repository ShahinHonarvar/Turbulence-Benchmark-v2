def lists_with_product_equal_n(lst):
    if not isinstance(lst, list) or len(lst) < 2:
        return []
    n = -15
    len_lst = len(lst)
    result = []
    for i in range(len_lst):
        product = 1
        for j in range(len_lst):
            index = (i + j) % len_lst
            product *= lst[index]
            if product == n:
                result.append(lst[i:index + 1])
    return result