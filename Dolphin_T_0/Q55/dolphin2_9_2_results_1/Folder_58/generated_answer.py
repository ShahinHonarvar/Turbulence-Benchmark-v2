import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:n // 2]
    result = set()
    for length in range(1, n + 1):
        for start_index in range(0, n):
            sublist = lst[start_index:start_index + length]
            if sublist[-1] * sublist[0] == 0:
                continue
            if sublist[-1] * sublist[0] == 1:
                result.add(tuple(sublist))
            else:
                for sublist_tuple in set(itertools.permutations(sublist, length)):
                    if sublist_tuple[0] * sublist_tuple[-1] == 733:
                        result.add(sublist_tuple)
    return [list(res) for res in result]