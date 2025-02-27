from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=76):

    def product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)

    def circular_sublists(numbers):
        for i in range(len(numbers)):
            yield list(islice(cycle(numbers), i, i + len(numbers)))
    return [sublist for sublist in circular_sublists(numbers) if product(sublist) == target]