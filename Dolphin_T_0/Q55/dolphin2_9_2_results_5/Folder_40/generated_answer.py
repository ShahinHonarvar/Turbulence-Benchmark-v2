def lists_with_product_equal_n(lst):
    size = len(lst)
    if size == 1:
        return []
    lst = lst + lst[:2]
    result = []
    product = 1
    for i in range(size):
        product *= lst[i]
        if product == -9:
            sub_lst = []
            for j in range(i + 1):
                product_sublist = 1
                for k in range(j, i + 1):
                    product_sublist *= lst[k]
                    sub_lst.append(lst[k])
                    if product_sublist == -9:
                        result.append(sub_lst[:])
                        sub_lst.pop()
            product = 1
    return result