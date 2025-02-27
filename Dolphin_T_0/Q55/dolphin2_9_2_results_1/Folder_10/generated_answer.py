def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        current_list = []
        for j in range(i, 0, -1):
            product *= lst[j]
            if product != -93:
                current_list.append(lst[j])
            elif product == -93:
                current_list.checked = True
                result.append(current_list[::-1])
                break
    return result