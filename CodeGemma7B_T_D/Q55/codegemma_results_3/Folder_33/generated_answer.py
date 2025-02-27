def lists_with_product_equal_n(circular_list):
    """
    this function returns list of sublists such that their product equals -115.
    """
    sublists = []
    for i in range(len(circular_list)):
        start_product = circular_list[i]
        product_list = [circular_list[i]]
        j = i + 1
        while j % len(circular_list) != i and j - i <= len(circular_list):
            start_product *= circular_list[j]
            product_list.append(circular_list[j])
            if start_product == -115:
                sublists.append(product_list)
            j += 1
    return sublists