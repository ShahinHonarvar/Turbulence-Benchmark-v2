def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(end):
                idx = (start + i) % n
                product *= circular_list[idx]
                sublist.append(circular_list[idx])
                if product == -69:
                    result.append(sublist[:])
    return result