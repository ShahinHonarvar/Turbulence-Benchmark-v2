def lists_with_product_equal_n(circular_list):
    n = 29
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                actual_index = current_index % length
                current_num = circular_list[actual_index]
                sublist.append(current_num)
                product *= current_num
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
                current_index += 1
    return result