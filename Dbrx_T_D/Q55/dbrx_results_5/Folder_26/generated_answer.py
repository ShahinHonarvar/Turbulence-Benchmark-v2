from more_itertools import circular_shifts

def product_of_sublist(sublist):
    return reduce(lambda x, y: x * y, sublist, 1)

def lists_with_product_equal_n(numbers):
    n = 93
    shifts = circular_shifts(numbers)
    sublists = [sublist for sublist in shifts if product_of_sublist(sublist) == n]
    return sublists