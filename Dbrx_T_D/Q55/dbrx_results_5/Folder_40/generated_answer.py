from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -9
    result = []
    for i in range(len(circular_list)):
        window = list(islice(cycle(circular_list[i:]), len(circular_list)))
        sublists = [window[j:j + k] for j in range(len(window)) for k in range(1, len(window) + 1)]
        valid_sublists = [sublist for sublist in sublists if n == sub_product(sublist)]
        result.extend(valid_sublists)
    return [list(sublist) for sublist in set((tuple(sublist) for sublist in result))]

def sub_product(sublist):
    return sub_product(sublist[1:]) * sublist[0] if sublist else 1