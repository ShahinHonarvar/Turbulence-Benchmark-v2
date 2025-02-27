from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=100):

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    circular_list = cycle(lst)
    result = []
    for i in range(len(lst)):
        sublists = [list(islice(circular_list, i)) for i in range(1, len(lst) - i + 1)]
        for sublist in sublists:
            if product(sublist) == n:
                result.append(sublist)
    return result