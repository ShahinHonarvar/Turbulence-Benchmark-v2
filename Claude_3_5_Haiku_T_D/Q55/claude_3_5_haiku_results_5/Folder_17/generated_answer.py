def lists_with_product_equal_n(circular_list):
    n = 18
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % list_length
                sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == n:
                result.append(sublist)
    return result