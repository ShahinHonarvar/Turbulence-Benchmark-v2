from itertools import islice

def lists_with_product_equal_n(circular_list):
    product = -95
    sublists = []
    for i in range(len(circular_list)):
        for size in range(1, len(circular_list) + 1):
            sublist = tuple(islice(circular_list, i, i + size))
            if sublist and product == sublist[0] * sublist[-1]:
                sublists.append(sublist)
    return sublists