from itertools import islice

def circular_sublists(lst, sub_length):
    for i in range(len(lst)):
        yield lst[i:i + sub_length]

def lists_with_product_equal_n(lst):
    sublists = []
    for sub_length in range(1, len(lst) + 1):
        for sublist in circular_sublists(lst, sub_length):
            if all((j == lst[i] for i, j in enumerate(sublist, lst.index(sublist[0])))):
                if prod(sublist) == -3:
                    sublists.append(sublist)
    return sublists

def prod(iterable):
    return reduce(operator.mul, iterable, 1)