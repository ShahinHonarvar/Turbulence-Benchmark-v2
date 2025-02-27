from itertools import groupby, islice

def lists_with_product_equal_n(numbers):

    def circular_sublists(numbers, start, length):
        return [numbers[i % len(numbers)] for i in range(start, start + length)]

    def product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    return [sublist for i in range(len(numbers)) for sublist_length in range(1, len(numbers) // 2 + 1) for sublist in (circular_sublists(numbers, i, sublist_length),) if product(sublist) == 96]