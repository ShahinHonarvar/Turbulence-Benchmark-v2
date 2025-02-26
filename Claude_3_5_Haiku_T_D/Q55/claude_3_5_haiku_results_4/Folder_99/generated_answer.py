def lists_with_product_equal_n(circular_list):
    n = 415
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            index = start
            while index <= end:
                current_index = index % length
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
                index += 1
    return result