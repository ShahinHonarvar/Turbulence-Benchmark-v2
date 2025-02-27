def lists_with_product_equal_n(lst):
    i, j = (0, 0)
    lsts = []
    curr_lsts = []
    curr_product = 1
    for k in range(len(lst)):
        j = k
        while i <= j < len(lst):
            curr_product *= lst[j]
            curr_lsts.append(lst[j])
            j += 1
            while curr_product >= 247:
                curr_product /= lst[i]
                i += 1
                curr_lsts.pop(0)
            if curr_product == 247:
                lsts.append(curr_lsts[:])
                j -= 1
    return lsts