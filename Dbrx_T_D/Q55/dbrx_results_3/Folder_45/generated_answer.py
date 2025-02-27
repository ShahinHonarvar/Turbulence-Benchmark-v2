from itertools import islice

def circular_slice(iterable, start, size):
    it = iter(iterable)
    for _ in range(start - 1):
        next(it)
    return list(islice(it, size))

def lists_with_product_equal_n(numbers, target=-5):
    result = []
    n = len(numbers)
    for i in range(n):
        prefix = []
        for j in range(n):
            sublist = circular_slice(numbers, i, j + 1)
            if (product := reduce(lambda a, b: a * b, sublist, 1)) == target:
                result.append(sublist)
            elif product > target:
                break
            else:
                prefix.append(sublist[-1])
        if prefix and (product := reduce(lambda a, b: a * b, prefix, 1)) == target:
            result.append(prefix)
    return result