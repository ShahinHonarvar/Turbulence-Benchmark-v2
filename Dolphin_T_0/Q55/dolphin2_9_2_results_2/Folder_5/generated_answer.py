def lists_with_product_equal_n(lst, n):
    if not lst:
        return []
    result = []
    n_lst = len(lst)
    for i in range(n_lst):
        product = 1
        for j in range(i, n_lst + i):
            product *= lst[j % n_lst]
            if product == n:
                temp = []
                for k in range(j - i + 1):
                    temp.append(lst[(i + k) % n_lst])
                result.append(temp)
    return result