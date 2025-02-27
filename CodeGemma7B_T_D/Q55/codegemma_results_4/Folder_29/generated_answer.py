from functools import reduce

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublists = []
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if reduce(lambda x, y: x * y, sublist) == 15:
                sublists.append(sublist)
        result.extend(sublists)
    return result