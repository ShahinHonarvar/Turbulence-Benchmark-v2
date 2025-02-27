from itertools import islice

def circular_list_iterator(lst):
    while True:
        for i in lst:
            yield i

def sliding_window(iterable, size):
    iter_ = iter(iterable)
    window = list(islice(iter_, size))
    if len(window) == size:
        yield window
    for item in iter_:
        window = window[1:] + [item]
        yield window

def lists_with_product_equal_n(lst, n):
    circular_lst = circular_list_iterator(list(lst))
    result = []
    for window in sliding_window(circular_lst, len(lst)):
        if len(window) == 1 and window[0] == 0:
            result.append(window)
        elif prod(window) == n:
            result.append(window)
    return result

def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1)