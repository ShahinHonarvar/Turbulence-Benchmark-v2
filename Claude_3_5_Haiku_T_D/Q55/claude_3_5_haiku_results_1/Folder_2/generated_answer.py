def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                real_index = current_index % n
                sublist.append(circular_list[real_index])
                product *= circular_list[real_index]
                if product == -968:
                    result.append(sublist.copy())
                current_index += 1
    return result