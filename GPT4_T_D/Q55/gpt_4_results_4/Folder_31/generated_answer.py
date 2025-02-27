def lists_with_product_equal_n(lst):
    orig_list = lst[:]
    result_lists = []
    for i in range(len(lst)):
        lst += [lst[i]]
    for i in range(len(orig_list)):
        for j in range(i + 1, len(orig_list) + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -16:
                result_lists.append(sublist)
    return result_lists