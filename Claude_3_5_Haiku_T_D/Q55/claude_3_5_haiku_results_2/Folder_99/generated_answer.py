def lists_with_product_equal_n(circular_list):
    n = 415
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            index = start
            while index <= end:
                current_value = circular_list[index % length]
                sublist.append(current_value)
                product *= current_value
                if product == n:
                    result.append(sublist.copy())
                    break
                elif product > n:
                    break
                index += 1
    return result