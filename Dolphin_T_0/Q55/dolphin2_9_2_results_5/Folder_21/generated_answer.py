def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = 851
    len_lst = len(lst)
    lst = lst + lst[:-1]
    result = []
    for i in range(len_lst):
        product = 1
        for j in range(i, len_lst + i):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if product > n:
                break
    return result