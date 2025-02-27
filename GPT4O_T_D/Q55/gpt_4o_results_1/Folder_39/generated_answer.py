def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            product = 1
            sublist = []
            for i in range(start, end + 1):
                idx = i % n
                product *= circular_list[idx]
                sublist.append(circular_list[idx])
                if product == -46:
                    result.append(sublist[:])
                    break
                if product == 0:
                    break
    return result