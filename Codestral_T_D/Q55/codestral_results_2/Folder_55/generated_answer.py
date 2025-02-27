def lists_with_product_equal_n(circular_list):
    n = -6
    sublists = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                sublists.append(circular_list[i:j + 1])
        if circular_list[i] == n:
            sublists.append([circular_list[i]])
        for j in range(i):
            product *= circular_list[j]
            if product == n:
                sublists.append(circular_list[j:i + 1])
    return sublists