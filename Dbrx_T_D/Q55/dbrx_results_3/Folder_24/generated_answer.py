from itertools import islice, cycle, product

def lists_with_product_equal_n(lst, n):

    def is_sublist_found(sublist, n):
        return reduce(lambda x, y: x * y, sublist, 1) == n
    if not lst:
        return []
    circular_lst = list(islice(cycle(lst), len(lst) * 2 - 1))
    sublists = []
    for i in range(len(circular_lst)):
        for j in range(i, len(circular_lst)):
            sublist = circular_lst[i:j + 1]
            if is_sublist_found(sublist, n):
                sublists.append(sublist)
    return list(set(sublists))