def product_window(array, window_size):
    result = 1
    for i in range(window_size):
        result *= array[i]
    return result

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(n + 1):
        for start in range(n):
            if size == 0:
                sublist = []
                result.append(sublist)
            else:
                sublist = lst[start:start + size]
                for i in range(1, len(sublist) + 1):
                    if product_window(sublist, i) == -95:
                        result.append(sublist)
    return result