def lists_with_product_equal_n(lst):

    def window(window_size):
        for i in range(len(lst)):
            yield lst[i:i + window_size]

    def circular_window(window_size):
        for i in range(len(lst)):
            yield (lst[i:] + lst[:i])
    result = []
    for window_size in range(1, len(lst) + 1):
        for circular_list in circular_window(window_size):
            for w in window(window_size):
                if len(w) == window_size and eval('*'.join(map(str, w))) == 51:
                    result.append(w)
    return result