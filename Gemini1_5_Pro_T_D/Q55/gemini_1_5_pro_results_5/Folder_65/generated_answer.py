def lists_with_product_equal_n(circular_list):
    n = 46
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if j > len(circular_list):
                sublist += circular_list[:j - len(circular_list)]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                sublists.append(sublist)
    return sublists