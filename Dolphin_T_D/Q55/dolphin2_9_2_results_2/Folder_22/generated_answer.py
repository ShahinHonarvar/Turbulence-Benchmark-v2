def lists_with_product_equal_n(lst):
    res = []
    list_len = len(lst)
    for i in range(list_len):
        product = 1
        for j in range(i, list_len + i):
            if j == i + 4:
                if product != 4:
                    break
                if lst[i:j] not in res:
                    res += [lst[i:j]]
            else:
                product *= lst[j % list_len]
    return res