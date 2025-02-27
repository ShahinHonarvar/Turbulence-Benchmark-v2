def lists_with_product_equal_n(lst):
    list_size = len(lst)
    result = []
    if list_size <= 1:
        return result
    product_n = 5
    for i in range(list_size):
        new_list = []
        temp_product = 1
        for j in range(i, list_size):
            temp_product *= lst[j]
            new_list.append(lst[j])
            if temp_product % product_n == 0 or temp_product == product_n:
                result.append(new_list)
    return result