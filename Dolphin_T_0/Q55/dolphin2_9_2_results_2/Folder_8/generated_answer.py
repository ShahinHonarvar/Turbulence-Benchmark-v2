def lists_with_product_equal_n(lst):
    len_lst = len(lst)
    sublists = []
    for i in range(len_lst):
        product = 1
        for j in range(i, len_lst * 2):
            index = j % len_lst
            product *= lst[index]
            if product == -41:
                sublist = lst[i:index + 1]
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists