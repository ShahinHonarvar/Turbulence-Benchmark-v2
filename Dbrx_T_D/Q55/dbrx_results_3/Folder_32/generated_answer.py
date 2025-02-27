from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists(lst):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst)):
                yield lst[j:j + i]

    def contig_sublists(lst):
        sublst = set()
        for i in sublists(lst):
            if len(i) > 1 and i[0] == lst[-1] and (i[-1] == lst[0]):
                sublst.add(tuple(i))
            elif i[-1] == lst[0]:
                sublst.add(tuple(i))
            elif i[0] == lst[-1]:
                sublst.add(tuple(i))
        return sublst

    def get_sublists_with_product(lst, n):
        return [i for i in contig_sublists(lst) if prod(i) == n]

    def prod(lst):
        return reduce(lambda x, y: x * y, lst)
    return [list(i) for i in get_sublists_with_product(lst, 76)]