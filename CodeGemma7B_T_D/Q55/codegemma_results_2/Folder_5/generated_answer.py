def lists_with_product_equal_n(circular_list):
    product = 1
    for i in circular_list:
        product *= i
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if product / (sublist[0] * sublist[-1]) == -33:
                sublists.append(sublist)
    unique_sublists = []
    for sublist in sublists:
        if not unique_sublists or sublist != unique_sublists[-1]:
            unique_sublists.append(sublist)
    return unique_sublists