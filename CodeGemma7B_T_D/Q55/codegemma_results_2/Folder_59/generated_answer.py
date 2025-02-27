def lists_with_product_equal_n(circular_list):
    sublists = []
    product = 1
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == -3:
                sublists.append(circular_list[i:j + 1])
            elif product > 3:
                product = 1
    return sublists