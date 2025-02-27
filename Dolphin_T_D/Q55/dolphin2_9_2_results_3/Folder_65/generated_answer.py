def lists_with_product_equal_n(lst):
    result = []
    _len = len(lst)
    for i in range(_len):
        if lst[i] == 46:
            result.append([46])
        else:
            product = lst[i]
            next_val = lst[(i + 1) % _len]
            for j in range(i + 2, _len + i):
                product *= next_val
                if next_val == 46:
                    result.append([46])
                elif product == 46:
                    result.append(lst[i:j % _len])
                next_val = lst[(j + 1) % _len]
    return result