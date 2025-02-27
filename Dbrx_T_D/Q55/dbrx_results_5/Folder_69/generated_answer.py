from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = list(islice(cycle(lst), i, i + len(lst)))
        if sublist[-1] * reduce(lambda x, y: x * y, sublist, 1) == 90:
            result.append(sublist)
    return result