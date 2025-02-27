from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    sublists = []
    for i in range(len(numbers)):
        window = list(islice(cycle(numbers), i, i + len(numbers)))
        if window and reduce(lambda x, y: x * y, window) == 18:
            sublists.append(window)
    return sublists

def reduce(func, iterable):
    iterator = iter(iterable)
    result = next(iterator)
    for element in iterator:
        result = func(result, element)
    return result