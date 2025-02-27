def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(end):
                index = (start + i) % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
                if product == -10:
                    result.append(sublist.copy())
    return result