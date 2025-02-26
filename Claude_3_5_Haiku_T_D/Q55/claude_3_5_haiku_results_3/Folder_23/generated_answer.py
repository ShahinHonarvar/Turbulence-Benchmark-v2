def lists_with_product_equal_n(circular_list):
    n = -95
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current = start
            while current <= end:
                index = current % length
                sublist.append(circular_list[index])
                product *= circular_list[index]
                current += 1
            if product == n:
                result.append(sublist)
    return result