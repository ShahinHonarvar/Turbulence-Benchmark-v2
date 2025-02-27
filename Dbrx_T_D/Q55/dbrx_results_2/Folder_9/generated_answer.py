from itertools import islice

def circular_slice(circular_list, start, end):
    if end < start:
        return circular_list[start:] + circular_list[:end]
    else:
        return circular_list[start:end]

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            if sublists and circular_list[i:j + 1] == sublists[-1]:
                continue
            if prod(circular_list[i:j + 1]) == -36:
                sublists.append(circular_list[i:j + 1])
    return sublists

def prod(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p