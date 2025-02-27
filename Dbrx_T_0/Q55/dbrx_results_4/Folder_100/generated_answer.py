from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        for i in range(len(lst)):
            yield from (lst[i:i + j] for j in range(1, len(lst) - i + 1))

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return [sl for sl in circular_sublists(lst) if product(sl) == 48]