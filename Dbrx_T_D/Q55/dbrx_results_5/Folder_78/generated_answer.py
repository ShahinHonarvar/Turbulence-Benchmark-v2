from itertools import islice

def circular_list_slice(circular_list, start, stop):
    if start < 0 or stop < 0:
        raise ValueError('Indices cannot be negative')
    return islice(itertools.chain(itertools.islice(circular_list, start, None), circular_list), 0, stop - start)

def sublists_with_product_equal_n(circular_list, n):
    if not circular_list:
        return []
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:]
        if reduce(lambda x, y: x * y, sublist, 1) == n:
            result.append(list(sublist))
        sublist = circular_list_list[0] + circular_list_list[-1]
        if reduce(lambda x, y: x * y, sublist, 1) == n:
            result.append(list(sublist))
        sublist = circular_list_list[0:i + 1]
        if reduce(lambda x, y: x * y, sublist, 1) == n:
            result.append(list(sublist))
    return result