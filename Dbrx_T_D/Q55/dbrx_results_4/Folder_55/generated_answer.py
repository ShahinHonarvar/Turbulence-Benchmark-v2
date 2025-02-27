from itertools import islice

def circular_list_slice(circular_list, start, end):
    return circular_list[start:end] + [circular_list[0]] if end > start else circular_list[start:end]

def circular_sublists(circular_list, length):
    return [circular_list_slice(circular_list, i, i + length) for i in range(len(circular_list))]

def lists_with_product_equal_n(circular_list):
    sublists = []
    for length in range(1, len(circular_list) + 1):
        for sublist in circular_sublists(circular_list, length):
            if all(sublist) and (length == 1 or sublist[0] != 0) and (length == 1 or sublist[-1] != 1):
                if reduce(lambda x, y: x * y, sublist) == -6:
                    sublists.append(sublist)
    return sublists