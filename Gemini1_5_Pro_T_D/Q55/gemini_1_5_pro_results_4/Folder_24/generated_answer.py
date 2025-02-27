def lists_with_product_equal_n(circular_list):
    n = -89
    sublists = []
    for start_index in range(len(circular_list)):
        for end_index in range(start_index, len(circular_list) + start_index):
            sublist = circular_list[start_index:end_index] + circular_list[:end_index - len(circular_list)] if end_index >= len(circular_list) else circular_list[start_index:end_index]
            if len(sublist) <= len(circular_list):
                product = 1
                for x in sublist:
                    product *= x
                if product == n:
                    sublists.append(sublist)
    return sublists