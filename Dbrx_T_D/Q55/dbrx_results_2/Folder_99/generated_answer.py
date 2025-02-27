from itertools import islice, chain

def lists_with_product_equal_n(numbers):

    def circular_slices(size):
        for i in range(len(numbers)):
            yield numbers[i:i + size]

    def product_without(number_list, number):
        return functools.reduce(lambda prod, num: prod * num, [n for n in number_list if n != number])
    n = 415
    result = []
    for size in range(1, len(numbers) + 1):
        for slice in circular_slices(size):
            if functools.reduce(lambda prod, num: prod * num, slice) == n:
                result.append(slice)
    return result