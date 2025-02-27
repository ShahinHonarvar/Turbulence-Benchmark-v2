def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -65
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            product = 1
            sublist = []
            for i in range(start, end):
                index = i % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
                if product == target_product:
                    result.append(sublist.copy())
    return result