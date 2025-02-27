def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 91:
                result.append(sublist.copy())
            if product == 0 or (product > 91 and product % 91 != 0):
                break
    return result