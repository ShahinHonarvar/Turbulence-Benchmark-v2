def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for window_size in range(1, len(lst) + 1):
            j = (i + window_size - 1) % len(lst)
            product *= lst[j]
            if product == 42:
                result.append(lst[i:j + 1] if i <= j else lst[i:] + lst[:j + 1])
            elif product > 42:
                break
    return result