def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            product = 1
            for i in range(length):
                current_index = (start + i) % n
                current_num = circular_list[current_index]
                sublist.append(current_num)
                product *= current_num
            if product == -1:
                result.append(sublist)
    return result