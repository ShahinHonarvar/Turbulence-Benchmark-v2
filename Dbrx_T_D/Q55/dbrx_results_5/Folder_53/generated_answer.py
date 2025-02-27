from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(sublist):
        n = 1
        for num in sublist:
            n *= num
        return n == -87
    sublists = []
    for i in range(len(circular_list)):
        sublist = list(islice(cyclic_sublist(circular_list, i), len(circular_list)))
        if find_sublists_with_product(sublist):
            sublists.append(sublist)
    return sublists

def cyclic_sublist(iterable, start):
    """Yield a cyclic sublist starting from start index."""
    lst = list(iterable)
    while True:
        yield lst[start]
        start += 1
        if start == len(lst):
            start = 0