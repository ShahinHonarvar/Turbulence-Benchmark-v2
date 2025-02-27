from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def circular_sublists(n):
        return (list(islice(cycle(numbers), i, i + n)) for i in range(len(numbers)))
    return [sublist for slen in range(1, len(numbers) + 1) for sublist in circular_sublists(slen) if functools.reduce(lambda x, y: x * y, sublist) == -56]