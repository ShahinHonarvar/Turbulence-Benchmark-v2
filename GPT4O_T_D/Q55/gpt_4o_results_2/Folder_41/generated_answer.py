def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            prod = 1
            sublist = []
            for i in range(start, start + end):
                index = i % n
                sublist.append(circular_list[index])
                prod *= circular_list[index]
                if prod == -20:
                    result.append(list(sublist))
    return result