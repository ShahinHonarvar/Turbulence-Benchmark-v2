def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    lst = lst + lst[:-1]
    sublists = []
    n_len = len(lst)
    for i in range(n_len):
        for j in range(i + 1, n_len):
            if lst[i:j + 1].__len__() <= lst.__len__() and lst[i:j + 1].__len__() >= i + 1:
                product = 1
                for k in lst[i:j + 1]:
                    product *= k
                if product == -87:
                    sublists.append(list(lst[i:j + 1]))
    return sublists