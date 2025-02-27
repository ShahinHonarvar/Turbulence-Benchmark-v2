def lists_with_product_equal_n(circular_list):
    n = 733
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        current_sublist = []
        for j in range(len(circular_list)):
            index = (i + j) % len(circular_list)
            product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if product == n:
                sublists.append(current_sublist)
    return sublists