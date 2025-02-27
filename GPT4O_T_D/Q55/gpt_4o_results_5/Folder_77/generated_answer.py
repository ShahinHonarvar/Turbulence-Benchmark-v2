def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target = 632
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= circular_list[index]
            if product == target:
                end = (index + 1) % n
                if end > start:
                    sublist = circular_list[start:end]
                else:
                    sublist = circular_list[start:] + circular_list[:end]
                result.append(sublist)
            if product == 0 or product > target:
                break
    return result