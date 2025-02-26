def lists_with_product_equal_n(circular_list):
    n = -61
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            index = start
            while index <= end:
                current = circular_list[index % length]
                sublist.append(current)
                product *= current
                if product == n:
                    result.append(sublist.copy())
                    break
                index += 1
    return result