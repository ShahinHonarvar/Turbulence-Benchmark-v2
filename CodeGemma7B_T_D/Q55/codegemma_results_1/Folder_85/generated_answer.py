def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        length = 1
        j = (i + 1) % len(circular_list)
        while j != i and product * circular_list[j] == -97:
            product *= circular_list[j]
            length += 1
            j = (j + 1) % len(circular_list)
        if product == -97:
            sublists.append(circular_list[i:i + length])
    return sublists