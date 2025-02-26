def lists_with_product_equal_n(circular_list):
    n = 32
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            current_sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % length
                current_sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == n:
                result.append(current_sublist)
    return result