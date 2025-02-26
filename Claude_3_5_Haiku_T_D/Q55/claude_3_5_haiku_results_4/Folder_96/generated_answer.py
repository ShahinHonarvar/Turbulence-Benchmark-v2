def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                current_value = circular_list[current_index]
                sublist.append(current_value)
                product *= current_value
                if product == 0:
                    result.append(sublist.copy())
                    break
    return result