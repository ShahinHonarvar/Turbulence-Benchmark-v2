from itertools import islice, groupby

def lists_with_product_equal_n(numbers):

    def circular_slice(numbers, start, length):
        return islice(numbers[start:] + numbers[:start], length)

    def circular_sublists(numbers, size):
        return [circular_slice(numbers, i, size) for i in range(len(numbers))]

    def product(sublist):
        return functools.reduce(lambda a, b: a * b, [1] + [i for i in sublist])
    sublists_of_all_sizes = [circular_sublists(numbers, i) for i in range(1, len(numbers) + 1)]
    sublists_with_product_93 = [sl for sl in sublists_of_all_sizes for sublist in sl if product(sublist) == 93]
    return sublists_with_product_93