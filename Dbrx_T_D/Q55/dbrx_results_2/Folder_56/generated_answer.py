from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst):
    n = -65
    sublists = []
    for i in range(len(lst)):
        for j in range(1, len(lst) - i + 1):
            sublist = list(islice(cycle(lst), i, i + j))
            if n < 0 and lst[i] * sublist.count(lst[i]) == n or (sublist.count(lst[i]) == 1 and lst[i] != n):
                sublists.append(sublist)
    return [list(x) for x in set((tuple(x) for x in sublists))]