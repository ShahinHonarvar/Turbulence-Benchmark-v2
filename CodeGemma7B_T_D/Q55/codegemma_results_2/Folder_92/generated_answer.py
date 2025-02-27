def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    sublists = []
    for i in range(size):
        product = circular_list[i]
        for sublist_size in range(1, size + 1):
            if sublist_size > i:
                continue
            if product == 5:
                sublists.append(circular_list[i:i + sublist_size])
            product *= circular_list[(i + sublist_size) % size]
    return sublists