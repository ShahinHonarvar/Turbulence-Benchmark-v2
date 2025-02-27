from itertools import cycle, islice

def lists_with_product_equal_n(cir_list):
    n = -8
    size = len(cir_list)
    res = []
    for win_size in range(1, size + 1):
        for start in range(size):
            cycled_list = islice(cycle(cir_list), start, start + size)
            window = list(islice(cycled_list, win_size))
            if len(window) < win_size:
                break
            product = 1
            for num in window:
                product *= num
            if product == n:
                res.append(window)
    return res