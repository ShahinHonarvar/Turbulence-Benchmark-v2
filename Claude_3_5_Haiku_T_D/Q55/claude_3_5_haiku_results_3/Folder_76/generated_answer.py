def lists_with_product_equal_n(circular_list):
    n = 247
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            i = start
            while i <= end:
                current_index = i % length
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
                i += 1
    return result