from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = 247
    sublists = []
    for i in range(len(circular_list)):
        sublist = list(islice(circular_list, i, len(circular_list) + i))
        if reduce(lambda x, y: x * y, sublist) == n:
            sublists.append(sublist)
    return sublists