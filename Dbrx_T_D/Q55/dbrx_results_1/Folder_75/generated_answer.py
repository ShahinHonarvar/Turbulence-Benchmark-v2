from itertools import islice, chain

def circular_last_element(lst):
    return lst[0] if not lst else lst[-1]

def circular_sublists(lst, size):
    return [lst[i:i + size] for i in range(len(lst) - size + 1)]

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n):

    def circular_sublists_with_product_equal_n(lst, n):
        for size in range(1, len(lst) + 1):
            for sl in circular_sublists(lst, size):
                if product(sl) == n:
                    yield sl
    return list(circular_sublists_with_product_equal_n(lst, n)) or lists_with_product_equal_n(chain(islice(lst, 1, None), [circular_last_element(lst)]), n)