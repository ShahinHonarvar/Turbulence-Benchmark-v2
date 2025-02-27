def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == 27:
                sublist = [circular_list[i % length] for i in range(start, end + 1)]
                result.append(sublist)
            if product == 0:
                break
    return result