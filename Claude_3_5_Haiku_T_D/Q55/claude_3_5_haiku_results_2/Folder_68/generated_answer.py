def lists_with_product_equal_n(circular_list):
    n = 6
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(1, length + 1):
            current_sublist = []
            product = 1
            for k in range(j):
                current_index = (i + k) % length
                current_num = circular_list[current_index]
                current_sublist.append(current_num)
                product *= current_num
            if product == n:
                result.append(current_sublist)
    return result