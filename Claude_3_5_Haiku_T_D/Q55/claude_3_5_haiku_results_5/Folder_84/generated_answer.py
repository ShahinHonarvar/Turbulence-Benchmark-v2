def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                curr_index = i % n
                sublist.append(circular_list[curr_index])
                product *= circular_list[curr_index]
            if product == -906 and sublist:
                result.append(sublist)
    return result