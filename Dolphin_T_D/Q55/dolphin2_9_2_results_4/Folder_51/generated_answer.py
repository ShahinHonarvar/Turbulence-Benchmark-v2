def lists_with_product_equal_n(lst, n):
    len_lst = len(lst)
    sublists = []
    product = 1
    for i in range(len_lst * 2):
        product *= lst[i % len_lst]
        if product == n:
            temp = []
            for j in range(i, i - len_lst, -1):
                temp += [lst[j % len_lst]]
            sublists.append(temp)
        elif i == len_lst * 2 - 1:
            if prod != 1:
                sublists = []
    return sublists