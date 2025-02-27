from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]] + [x for x in islice(cycle(lst), i + 1, i + len(lst))]
        if sublst[0] != 0 and all((x != 0 for x in sublst[1:])) and (sublst[::2] + sublst[1::2] == sorted(sublst)) and (sublst[0] * (sublst[1] * ... * sublst[-1]) == 15):
            result.append(sublst)
    return result