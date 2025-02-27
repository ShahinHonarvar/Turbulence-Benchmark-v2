from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def circular_slice(lst, start, end):
        return islice(cycle(lst), start, end)

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    n = -94
    circular_lst = cycle(lst)
    window_size = 1
    result = []
    while window_size <= len(lst):
        for i in range(len(lst) - window_size + 1):
            window = list(circular_slice(circular_lst, i, i + window_size))
            if product(window) == n:
                result.append(window)
        window_size += 1
    return result