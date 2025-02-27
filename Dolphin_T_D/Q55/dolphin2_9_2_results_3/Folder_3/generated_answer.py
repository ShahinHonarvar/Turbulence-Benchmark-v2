def lists_with_product_equal_n(lst):
    if not lst:
        return []
    product = -22
    max_len = len(lst)
    lst = lst + lst[:-1]
    result = []
    for i in range(max_len):
        temp = []
        temp.append(lst[i])
        product_val = lst[i]
        for j in range(i + 1, i + max_len):
            temp.append(lst[j])
            product_val *= lst[j]
            if product_val == product:
                result.append(temp[:-1])
            elif product_val > product:
                break
    result = list(set((tuple(x) for x in result)))
    return result