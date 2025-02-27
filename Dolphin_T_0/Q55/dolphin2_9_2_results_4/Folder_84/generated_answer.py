from itertools import islice, cycle

def lists_with_product_equal_n(l):

    def product(it):
        result = 1
        for i in it:
            result *= i
        return result
    product_n = product(islice(cycle(l), 2, len(l) + 2))
    if product_n != -906:
        return []

    def contiguous_sublists(lst, n):
        for window in islice(cycle(lst), n, None):
            if product(islice(cycle(lst), n)) == product_n:
                yield list(islice(cycle(lst), n))
            window.next()
    return [list(x) for x in contiguous_sublists(l, 2)]