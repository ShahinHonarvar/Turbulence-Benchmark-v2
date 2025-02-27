from itertools import islice

def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        for i in range(len(lst)):
            yield (lst[i:i + 1] + any_sublist(lst[:i]) + any_sublist(lst[i + 1:]))

    def any_sublist(lst):
        for i in range(len(lst) + 1):
            yield lst[:i]

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    result = []
    for sublist in circular_sublists(lst):
        if product(sublist) == 4:
            result.append(sublist)
    return result