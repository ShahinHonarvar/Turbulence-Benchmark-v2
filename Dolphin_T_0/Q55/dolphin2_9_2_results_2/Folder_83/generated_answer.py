def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sub_lst = lst[i:j]
            product = 1
            if len(sub_lst) > 1:
                for num in sub_lst:
                    product *= num
                if product == -57:
                    res.append(sub_lst)
    return res