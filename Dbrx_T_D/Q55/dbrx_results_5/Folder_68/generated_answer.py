from itertools import islice

def lists_with_product_equal_n(numbers):

    def is_circular_slice(slc, n):
        if len(slc) == 0:
            return False
        if 6 % prod(slc) == 0:
            return 6 // prod(slc) == 1 or 6 // prod(slc) == 3
        return False

    def prod(iterable):
        result = 1
        for i in iterable:
            result *= i
        return result
    sublists = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sublists.append(tuple(islice(numbers, i, j)))
    result = [sublist for sublist in sublists if is_circular_slice(sublist, n)]
    return result