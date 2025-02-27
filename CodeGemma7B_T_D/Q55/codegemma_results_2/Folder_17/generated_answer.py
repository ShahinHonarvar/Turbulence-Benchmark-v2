def lists_with_product_equal_n(lst):
    sublists = []
    lst = lst + lst
    for start in range(len(lst)):
        for end in range(start + 2, len(lst)):
            curr_product = lst[start]
            sublist = [curr_product]
            for i in range(start + 1, end):
                curr_product *= lst[i]
                sublist.append(lst[i])
            if curr_product == product:
                sublists.append(sublist)
    return sublists