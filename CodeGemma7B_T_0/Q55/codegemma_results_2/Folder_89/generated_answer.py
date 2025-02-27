def lists_with_product_equal_n(circular_list):
    """
            This function takes a circular list of integers and returns a list of sublists
            each of which contains the contiguous integers from the given list such that
            their product equals 57.
            """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k]
            if product == 57:
                sublists.append(circular_list[i:j + 1])
    return sublists