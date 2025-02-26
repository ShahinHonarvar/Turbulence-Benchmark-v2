def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
            if product == 3:
                result.append(sublist)
    return result