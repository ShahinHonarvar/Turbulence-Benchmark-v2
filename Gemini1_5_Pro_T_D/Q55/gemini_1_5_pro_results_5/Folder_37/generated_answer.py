def lists_with_product_equal_n(circular_list):
    n = -76
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if j - i + 1 < len(circular_list):
                sublist += circular_list[:j - len(circular_list) + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists