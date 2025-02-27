from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        if not lst:
            return []
        elif lst[0] * n == -9:
            return [[lst[0]]]
        else:
            return sublists_with_product_equal_n(lst[1:], n * lst[0]) + sublists_with_product_equal_n(lst[1:], n)

    def circular_sublists(lst, size):
        if size > len(lst):
            return []
        else:
            return [lst[i:i + size] for i in range(len(lst))] + circular_sublists(lst, size + 1)
    return [sublist for size in range(1, len(lst) + 1) for sublist in circular_sublists(lst, size) if sublists_with_product_equal_n(sublist, 1)]