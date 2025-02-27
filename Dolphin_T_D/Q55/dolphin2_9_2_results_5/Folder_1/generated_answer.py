def lists_with_product_equal_n(lst):
    product = -51
    length = len(lst)
    sub_lists = []
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub = lst[i:j]
            sub_product = 1
            for k in sub:
                sub_product *= k
            if sub_product == product:
                sub_lists.append(sub)
    return sub_lists