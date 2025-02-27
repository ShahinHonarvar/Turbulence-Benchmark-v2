def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= circular_list[end]
            if product == -26:
                sublist = []
                for i in range(size):
                    index = (start + i) % n
                    sublist.append(circular_list[index])
                result.append(sublist)
            if end == start - 1:
                break
    return result