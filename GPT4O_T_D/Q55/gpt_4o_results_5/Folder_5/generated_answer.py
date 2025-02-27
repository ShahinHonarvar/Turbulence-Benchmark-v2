def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(1, length + 1):
            prod = 1
            sublist = []
            for i in range(end):
                current = circular_list[(start + i) % length]
                sublist.append(current)
                prod *= current
                if prod == -33:
                    result.append(sublist.copy())
    return result