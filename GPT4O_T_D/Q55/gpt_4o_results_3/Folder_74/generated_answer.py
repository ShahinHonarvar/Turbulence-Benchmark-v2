def lists_with_product_equal_n(circular_list):
    n = 51
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        sublist = []
        for i in range(size):
            idx = (start + i) % size
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == n:
                result.append(sublist.copy())
            if product > n or len(sublist) >= size:
                break
    return result