from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -779
    sublists = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if i > 0 and sublist[:i] == sublist[-i:]:
            continue
        if product(sublist) == n:
            sublists.append(sublist)
    return sublists

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)