from itertools import islice, cycle

def sublists_with_product_equal_n(lst, n):

    def circular_sublists(lst):
        return (lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1))

    def product_of_sublist(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    return [sublist for sublist in circular_sublists(lst) if product_of_sublist(sublist) == n]

def lists_with_product_equal_n(lst, n):
    return [sublist for sublist in lst if sublists_with_product_equal_n([lst[i] for i in range(len(lst)) if j != i], n)] if n != 0 else []