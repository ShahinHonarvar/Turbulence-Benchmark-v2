from itertools import islice, cycle

def circular_slice(iterable, start, stop):
    it = iter(iterable)
    slice = islice(it, start, stop)
    return list(cycle(slice))

def lists_with_product_equal_n(lst, n):
    result = []
    for length in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublst = circular_slice(lst, i, i + length)
            if reduce(lambda x, y: x * y, sublst, 1) == n:
                result.append(sublst)
    return result