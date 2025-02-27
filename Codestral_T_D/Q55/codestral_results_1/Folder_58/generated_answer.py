def lists_with_product_equal_n(circular_list):
    sublists = []
    n = 733
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                sublists.append(sublist)
            if product > n:
                break
        for j in range(i):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                sublists.append(sublist)
            if product > n:
                break
    return sublists