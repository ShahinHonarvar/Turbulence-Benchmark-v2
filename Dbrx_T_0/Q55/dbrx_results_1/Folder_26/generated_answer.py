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
                elif n == 1:
                    continue
                elif not sublist:
                    continue
                elif reduce(lambda x, y: x * y, sublist) == n:
                    yield sublist
                elif reduce(lambda x, y: x * y, sublist) < n:
                    for k in sublists_with_product_equal_n(sublist, n / reduce(lambda x, y: x * y, sublist)):
                        yield k
    return list(set(sublists_with_product_equal_n(lst, 93)))