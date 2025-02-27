from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1 and (not sublist):
                    yield []
                elif n == 1 and sublist:
                    yield sublist
                elif sublist and n % sublist[0] == 0:
                    yield from sublists_with_product_equal_n(sublist[1:], n // sublist[0])
    return list(set(sublists_with_product_equal_n(lst, 990)))

def circular_sublists(lst):
    for i in range(len(lst)):
        yield from (lst[i:] + lst[:i])

def circular_lists_with_product_equal_n(lst):
    return lists_with_product_equal_n(list(circular_sublists(lst)))