def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst_len = len(lst)
    result = []
    product_dict = dict()
    for i in range(lst_len):
        product = lst[i]
        for j in range(i + 1, lst_len + 1):
            if j == lst_len:
                j = 0
            if product == -17 and product not in product_dict:
                result.append(lst[i:j])
                product_dict[product] = lst[i:j]
            elif product == -17:
                result.append(lst[i:j])
            if product == -17:
                break
            else:
                product *= lst[j]
    return result