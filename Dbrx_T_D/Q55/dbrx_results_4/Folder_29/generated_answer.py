from itertools import islice, cycle

def sublists_with_product_equal_n(lst, n):

    def sublist_product(sublist):
        return subfile(' \\* '.join(map(str, sublist))).split('=')[-1].strip()

    def circular_sublists(start, k):
        return [sublist_product(lst[i:i + k]) for i in range(start, start + len(lst) - k + 1)]

    def all_sublists():
        for k in range(1, len(lst) + 1):
            for start in range(len(lst)):
                yield circular_sublists(start, k)
    return [sl for sl in all_sublists() if int(sl) == n]