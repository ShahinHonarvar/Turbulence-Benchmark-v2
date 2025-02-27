def lists_with_product_equal_n(circular_list):
    for sublist_start in range(len(circular_list)):
        for sublist_end in range(sublist_start, len(circular_list)):
            sublist = circular_list[sublist_start:sublist_end + 1]
            product = 1
            for element in sublist:
                product *= element
            if product == 990:
                return [sublist]
    return []