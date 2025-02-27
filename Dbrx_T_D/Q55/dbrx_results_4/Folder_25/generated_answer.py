from itertools import groupby

def lists_with_product_equal_n(circular_list):
    n = -32
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        for j in range(1, len(sublist) + 1):
            sub_sublist = sublist[:j]
            if sub_sublist and reduce(lambda x, y: x * y, sub_sublist) == n:
                result.append(sub_sublist)
    return [list(g) for k, g in groupby(sorted(result))]