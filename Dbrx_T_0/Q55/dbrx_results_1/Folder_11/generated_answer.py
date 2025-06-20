from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst), i, i + len(lst)))
        if window and window[0] * window[-1] == -15:
            result.append(window)
    return result