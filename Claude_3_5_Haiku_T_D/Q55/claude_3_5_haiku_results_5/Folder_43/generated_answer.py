def lists_with_product_equal_n(circular_list):
    n = -26
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_value = circular_list[current_index % length]
                sublist.append(current_value)
                product *= current_value
                if product == n:
                    result.append(sublist.copy())
                    break
                if product < n or current_index == end:
                    break
                current_index += 1
    return result