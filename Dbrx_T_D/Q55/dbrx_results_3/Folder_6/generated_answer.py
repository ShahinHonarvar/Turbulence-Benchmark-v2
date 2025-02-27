from itertools import islice

def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst, size):
        for i in range(len(lst)):
            yield lst[i:i + size]
    sublists = []
    for i in range(1, len(circular_list) + 1):
        for sublist in circular_sublists(circular_list, i):
            if prod(sublist) == 42:
                sublists.append(sublist)
    return sublists

def prod(xs):
    return reduce(lambda x, y: x * y, xs, 1)