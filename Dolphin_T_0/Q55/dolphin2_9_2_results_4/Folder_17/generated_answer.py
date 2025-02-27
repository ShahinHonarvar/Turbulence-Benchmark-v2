def lists_with_product_equal_n(lst):
    result = []
    lst_length = len(lst)
    product = 1
    for i in range(lst_length):
        product = 1
        for j in range(lst_length):
            product *= lst[(i + j) % lst_length]
            if product == 18:
                result.append(lst[i:i + j + 1])
    return result