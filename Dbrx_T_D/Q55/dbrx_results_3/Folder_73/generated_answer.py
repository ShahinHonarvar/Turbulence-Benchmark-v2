from itertools import islice

def circular_slice(iterable, start_index, length):
    return islice(iterable, start_index, start_index + length) or islice(iterable, start_index % len(iterable), start_index % len(iterable) + length)

def product(iterable):
    return reduce(lambda x, y: x * y, iterable)

def circular_sublists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = circular_slice(lst, i, j - i + 1)
            if product(sublist) == n:
                result.append(list(sublist))
    return result