from itertools import islice, combinations

def lists_with_product_equal_n(lst):

    def circular_sublists(lst, r):
        return islice(combinations(lst, r), 1, None)

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return [sl for sl in circular_sublists(lst, len(lst) - 1) if product(list(sl)) == 632]