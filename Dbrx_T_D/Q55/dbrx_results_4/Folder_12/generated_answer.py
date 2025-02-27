from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = -18
    result = []
    for i in range(len(numbers)):
        window = list(islice(cycle(numbers), i, i + len(numbers)))
        if window and window[0] * window[-1] == n:
            result.append(window)
    return result