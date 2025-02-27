def lists_with_product_equal_n(lst, n=-8):
    len_lst, res = (len(lst), [])
    for i in range(len_lst):
        product = 1
        if lst[i] == 0:
            if n == 0:
                res.append([0])
            continue
        for j in range(i, len_lst * 2):
            product *= lst[j % len_lst]
            if product == n:
                res.append(lst[i:j % len_lst + 1])
            elif product > n:
                break
    return res