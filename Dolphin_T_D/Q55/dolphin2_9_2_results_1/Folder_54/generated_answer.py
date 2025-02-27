def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst_len = len(lst)
    indices = list(((i, i - 1) for i in range(lst_len)))
    sub_lst = [[lst[i] for i in range(j, k + 1)] for j, k in indices]
    product = [-17]
    result = [s for s in sub_lst if prod(s) in product]
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p