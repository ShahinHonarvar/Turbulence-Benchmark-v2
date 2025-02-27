def lists_with_product_equal_n(lst):
    n = 8
    circ_lst = lst * 2
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, i + len(lst)):
            prod = 1
            for k in range(i, j + 1):
                prod *= circ_lst[k]
                if prod == n:
                    res.append(circ_lst[i:j + 1])
                elif prod > n:
                    break
            if prod < n:
                break
    return res