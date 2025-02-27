def lists_with_product_equal_n(circular_list):
    n = -97
    result = []
    list_len = len(circular_list)
    for start in range(list_len):
        for end in range(1, list_len + 1):
            product = 1
            sublist = []
            for i in range(start, start + end):
                index = i % list_len
                product *= circular_list[index]
                sublist.append(circular_list[index])
                if product == n:
                    result.append(sublist[:])
                    break
                elif product < 0 and abs(product) > abs(n):
                    break
    return result