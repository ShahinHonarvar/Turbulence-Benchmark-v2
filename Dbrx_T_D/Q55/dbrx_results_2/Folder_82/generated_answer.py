from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 8
    sublists = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list[i:]), i, i + len(circular_list[i:])))
        if sublist and reduce(lambda x, y: x * y, sublist, 1) == n:
            sublists.append(sublist)
    return sublists