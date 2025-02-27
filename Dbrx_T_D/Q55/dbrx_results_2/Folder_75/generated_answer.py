from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def product_sublist(sublist):
        return len(sublist) > 0 and int(not sublist[0] == 1) * reduce(lambda x, y: x * y, sublist) == 13
    return [sublist for i in range(len(circular_list)) for sublist in is_sublists_of_size(i, itertools.islice(cycle(circular_list), i, i + len(circular_list))) if product_sublist(sublist)]

def is_sublists_of_size(size, iterable):
    if size == 0:
        yield []
        return
    for i in range(len(list(iterable)) - size + 1):
        for x in is_sublists_of_size(size - 1, iterable):
            yield ([iterable[i]] + x)