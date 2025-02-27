from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-779):

    def product(lst):
        return functools.reduce(lambda x, y: x * y, lst, 1)

    def circular_sublists(lst):
        return (list(islice(lst, i, None)) + list(islice(lst, i)) for i in range(1, len(lst) + 1))

    def possible_sublists(lst):
        return (sl for sl in circular_sublists(lst) if any((product(sub) == target for sub in circular_sublists(sl))))
    return list(possible_sublists(numbers))