def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for count in range(n):
            idx = (start + count) % n
            sublist.append(circular_list[idx])
            product *= circular_list[idx]
            if product == 2:
                result.append(sublist[:])
            if product != 0 and (product > 2 or n == count + 1):
                break
    return result