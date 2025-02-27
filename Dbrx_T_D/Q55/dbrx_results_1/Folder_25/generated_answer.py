def lists_with_product_equal_n(lst):
    n = -32
    result = []
    for i in range(len(lst)):
        current_product = 1
        current_list = []
        for j in range(i, len(lst)):
            current_list.append(lst[j])
            current_product *= lst[j]
            if current_product == n:
                result.append(current_list.copy())
            elif current_product > n:
                break
    return result