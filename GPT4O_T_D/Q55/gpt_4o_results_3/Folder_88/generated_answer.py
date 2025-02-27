def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            product = 1
            sublist = []
            for i in range(start, end + 1):
                index = i % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == -56:
                    result.append(sublist.copy())
    return result