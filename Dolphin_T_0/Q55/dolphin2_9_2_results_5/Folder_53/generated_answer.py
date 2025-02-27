def lists_with_product_equal_n(circular_list, n):
    sublists = []
    list_length = len(circular_list)
    for i in range(list_length):
        product = 1
        for j in range(i, list_length):
            product *= circular_list[j]
            if product == n:
                sublists.append(circular_list[i:j + 1])
            if product > n:
                break
    if sublists == []:
        return []
    else:
        return sublists