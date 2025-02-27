def lists_with_product_equal_n(lst):

    def all_sublists(lst):
        sub_lsts = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sub_lsts.append(lst[i:j + 1])
        return sub_lsts
    result = []
    all_lsts = all_sublists(lst)
    for lst in all_lsts:
        product = 1
        for num in lst:
            product *= num
        if product == -57:
            result.append(lst)
    return result