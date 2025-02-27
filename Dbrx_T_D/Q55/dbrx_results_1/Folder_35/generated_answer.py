from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def cyclic_slice(index, length):
        return islice(cycle(numbers), index, index + length)

    def sublist_product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    return [sublist for sublist in (list(cyclic_slice(i, j)) for i in range(len(numbers)) for j in range(1, len(numbers) - i + 1)) if sublist_product(sublist) == n]