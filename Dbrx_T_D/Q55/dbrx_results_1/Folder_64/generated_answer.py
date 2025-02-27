from itertools import islice

def sublists_with_product_equal_n(lst, n=3):

    def circular_slice(lst, start, end):
        return lst[start % len(lst):end] + lst[:start % len(lst)]

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return [sl for sl in (circular_slice(lst, i, j) for i in range(len(lst)) for j in range(i, len(lst) + 1)) if product(sl) == n and sl]