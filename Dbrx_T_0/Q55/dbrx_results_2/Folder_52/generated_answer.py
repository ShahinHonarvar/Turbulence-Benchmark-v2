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
                elif sublist and sublist[0] % n == 0 and all((x % n == 0 for x in sublist[1:])):
                    yield from (sublist[:1] + s for s in sublists_with_product_equal_n(sublist[1:], n // sublist[0]))
    return list(set((tuple(sorted(sublist)) for sublist in sublists_with_product_equal_n(lst, 37) if sublist)))