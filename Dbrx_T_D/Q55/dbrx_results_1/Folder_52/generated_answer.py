from itertools import chain, combinations

def lists_with_product_equal_n(circular_list):
    n = 37
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(list(chain.from_iterable(combinations(circular_list, i))))
    return [sublist for sublist in sublists if prod(sublist) == n]

def prod(nums):
    return reduce(lambda x, y: x * y, nums, 1)