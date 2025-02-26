def lists_with_product_equal_n(circular_list):
    n = 90
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for j in range(start, end + 1):
                index = j % length
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == n:
                result.append(sublist)
    return result