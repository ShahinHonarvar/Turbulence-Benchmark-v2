def lists_with_product_equal_n(clist):
    sublists = []
    current_product = 1
    start_index = 0
    for end_index, number in enumerate(clist):
        current_product *= number
        if current_product == -33:
            sublists.append(clist[start_index:end_index + 1])
        elif current_product > -33:
            current_product = 1
            start_index = end_index + 1
    return sublists