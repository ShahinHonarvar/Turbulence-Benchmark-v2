def lists_with_product_equal_n(circular_list):
    n = -65
    product = 1
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                sublists.append(circular_list[i:j + 1])
            elif product > n:
                break
        product = 1
    return sublists