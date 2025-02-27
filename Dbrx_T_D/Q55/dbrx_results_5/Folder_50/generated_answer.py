from itertools import islice, cycle

def lists_with_product_equal_n(circular_list, n=45):

    def contiguous_sublists(lst):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                yield lst[j:j + i]
    circular_list = list(circular_list)
    result = []
    for sublist in contiguous_sublists(circular_list):
        if isinstance(sublist, int):
            sublist = [sublist]
        if n in (p := tuple(sublist)):
            result.append(sublist)
            continue
        circular_sublist = deque(islice(cycle(sublist), n - p.index(1) - 1, n - p.index(1) + len(sublist)))
        if all((x * y == n for x, y in zip(circular_sublist, circular_sublist[1:]))):
            result.append(list(circular_sublist))
    return result