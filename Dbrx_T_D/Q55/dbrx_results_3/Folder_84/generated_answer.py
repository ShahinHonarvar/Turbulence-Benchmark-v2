from itertools import islice, chain

def lists_with_product_equal_n(circular_list):
    n = -906
    sublists = []
    for i in range(len(circular_list)):
        sublist = list(islice(chain(circular_list[i:], circular_list[:i]), len(circular_list)))
        if reduce(lambda x, y: x * y, sublist) == n:
            sublists.append(sublist)
    return sublists