def lists_with_product_equal_n(lst):
    n = len(lst)
    sub_list = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j % n]
            if product == -44:
                sub_list.append(lst[i:j % n + 1])
    return sub_list