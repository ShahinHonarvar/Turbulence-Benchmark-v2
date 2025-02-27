def lists_with_product_equal_n(circular_list):
    products = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == -16:
                products.append(sublist[:])
                break
            elif product > -16:
                break
    return products