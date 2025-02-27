def lists_with_product_equal_n(lst, n=-54):
    size_lst = len(lst)
    if size_lst == 0:
        return []
    result = []
    for i in range(size_lst):
        product = lst[i]
        if product == n:
            result.append([lst[i]])
        sub = [lst[i]]
        j = (i + 1) % size_lst
        while j != i:
            product *= lst[j]
            if product > n:
                break
            if product == n:
                result.append(sub + [lst[j]])
            sub.append(lst[j])
            j = (j + 1) % size_lst
    return result