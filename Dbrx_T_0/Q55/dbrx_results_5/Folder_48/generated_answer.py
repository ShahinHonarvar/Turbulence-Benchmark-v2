from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1 and (not sublist):
                    yield []
                elif n == 1 and sublist[0] == 1:
                    yield sublist
                elif n % sublist[0] == 0:
                    for k in sublists_with_product_equal_n(sublist[1:], n // sublist[0]):
                        yield ([sublist[0]] + k)
    return list(set(sublists_with_product_equal_n(lst, 990)))

def circular_sublists(lst):
    for i in range(len(lst)):
        yield list(islice(cycle(lst), i, i + len(lst)))

def filter_circular_sublists(sublists):
    seen = set()
    for sublist in sublists:
        if tuple(sublist) not in seen:
            yield sublist
            seen.add(tuple(sublist))

def lists_with_product_equal_n_circular(lst):
    return list(filter_circular_sublists(circular_sublists(lst)))