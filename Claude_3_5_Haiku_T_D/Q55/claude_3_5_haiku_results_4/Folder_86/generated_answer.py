def lists_with_product_equal_n(circular_list):
    n = -779
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % length
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
            if product == n and sublist:
                result.append(sublist)
    return result