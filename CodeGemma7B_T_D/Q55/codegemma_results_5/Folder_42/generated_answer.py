def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, len(circular_list)):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == 25 and len(sublist) <= len(circular_list):
                yield sublist
            elif product > 25:
                product = 1
                sublist = []