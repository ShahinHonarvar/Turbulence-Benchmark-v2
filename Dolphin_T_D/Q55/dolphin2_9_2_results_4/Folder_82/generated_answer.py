def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:2]
    result = []
    for i in range(n):
        product = lst[i]
        if product == 8:
            result.append([lst[i]])
        sub_list = [lst[i]]
        for j in range(i + 1, n + 2):
            sub_list.append(lst[j])
            product *= lst[j]
            if product == 8:
                result.append(sub_list.copy())
            if product > 8:
                break
    return result