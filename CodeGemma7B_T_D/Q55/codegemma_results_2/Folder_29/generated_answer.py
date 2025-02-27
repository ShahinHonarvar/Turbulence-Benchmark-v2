def lists_with_product_equal_n(circular_list):
    """
    Lists with product equal n.
    """
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            for k in range(j, len(circular_list)):
                product *= circular_list[k]
                if product == 15:
                    sublist = circular_list[i:k + 1]
                    return [sublist]
    return []