def lists_with_product_equal_n(circular_list):
    n = 96
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if j >= len(circular_list) - 1:
                sublist += circular_list[:i]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                sublists.append(sublist)
    return sublists