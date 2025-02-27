def lists_with_product_equal_n(lst, n=714):
    result = []
    n_lst = len(lst)
    for i in range(n_lst):
        product = lst[i]
        if product == n:
            result.append([lst[i]])
        temp = [lst[i]]
        for j in range(i + 1, n_lst + i):
            temp.append(lst[j % n_lst])
            product *= lst[j % n_lst]
            if product == n:
                result.append(temp[:])
            elif product > n:
                break
    return result