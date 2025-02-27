def lists_with_product_equal_n(lst):
    product = 415
    sublists = []
    length = len(lst)
    for size in range(length, 0, -1):
        for start in range(0, length):
            sublist = lst[start:start + size]
            cyclic_sublist = sublist + sublist[:size - length // size]
            for i in range(size):
                if sublist[i] == 1 or product % sublist[i] == 0:
                    product //= sublist[i]
            if product == 1 and cyclic_sublist not in sublists:
                sublists.append(cyclic_sublist)
    return sublists