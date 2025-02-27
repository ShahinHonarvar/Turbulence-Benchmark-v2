def lists_with_product_equal_n(n, circular_list):
    result = []
    list_len = len(circular_list)
    for i in range(list_len):
        product = 1
        sublist = []
        for j in range(i, i + list_len):
            sublist.append(circular_list[j % list_len])
            product *= circular_list[j % list_len]
            if product > n:
                break
            if product == n:
                result.append(sublist)
    return result