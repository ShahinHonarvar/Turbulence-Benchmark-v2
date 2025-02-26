def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                idx = i % n
                sublist.append(circular_list[idx])
                product *= circular_list[idx]
            if product == -15:
                result.append(sublist)
    return result