def lists_with_product_equal_n(circular_list):
    n = 51
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if j == len(circular_list) and i != 0:
                sublist += circular_list[0:i]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
    return sublists