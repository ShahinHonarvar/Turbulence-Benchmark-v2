from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-89):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst), i, i + len(lst)))
        if window and reduce(lambda x, y: x * y, window) == n:
            result.append(window)
    return result