def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            idx = (start + length - 1) % n
            product *= circular_list[idx]
            if product == 37:
                sublist = []
                for i in range(length):
                    sublist.append(circular_list[(start + i) % n])
                result.append(sublist)
            if length == n:
                break
    return result