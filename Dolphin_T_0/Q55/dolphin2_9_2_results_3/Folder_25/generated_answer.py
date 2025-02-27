def lists_with_product_equal_n(lst):
    sublists = []
    lst_len = len(lst)
    lst_product = 1
    start = 0
    for i in range(lst_len):
        lst_product *= lst[i]
        while lst_product > 32 and start < i:
            lst_product //= lst[start]
            start += 1
        if lst_product == 32:
            sublists.append(lst[start:i + 1])
    return sublists