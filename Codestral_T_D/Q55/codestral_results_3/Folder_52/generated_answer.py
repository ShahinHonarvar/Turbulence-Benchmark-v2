def lists_with_product_equal_n(lst):
    n = 37
    length = len(lst)
    circ_lst = lst * 2
    result = []
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, i + length):
            product *= circ_lst[j]
            sublist.append(circ_lst[j])
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result