def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []
    total_length = len(lst)
    for i in range(total_length):
        prod_list = [lst[i]]
        product = lst[i]
        for j in range(1, total_length + 1):
            if product * lst[(i + j) % total_length] == -6:
                prod_list.append(lst[(i + j) % total_length])
                product *= lst[(i + j) % total_length]
            else:
                break
        if product == -6:
            result.append(prod_list)
    return result