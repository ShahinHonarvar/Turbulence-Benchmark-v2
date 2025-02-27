def lists_with_product_equal_n(circular_list):
    """Finds contiguous sublists with product equal to -94."""
    product = 1
    sublists = []
    start = 0
    for i, num in enumerate(circular_list):
        product *= num
        if product == -94:
            sublists.append(circular_list[start:i + 1])
        elif product > -94:
            while product > -94:
                product /= circular_list[start]
                start += 1
            if product == -94:
                sublists.append(circular_list[start:i + 1])
    return sublists