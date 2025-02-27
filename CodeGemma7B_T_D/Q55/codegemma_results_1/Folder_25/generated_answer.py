def lists_with_product_equal_n(circular_list):
    """Returns a list of contiguous sublists whose product is -32."""
    product = -32
    sublists = []
    for i in range(len(circular_list)):
        current_product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            current_product *= circular_list[j]
            if current_product == product:
                sublists.append(circular_list[i:j + 1])
            elif current_product > product:
                break
    return sublists