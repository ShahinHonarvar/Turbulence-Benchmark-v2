def lists_with_product_equal_n(circular_list):
    n = 32
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_value = circular_list[current_index % list_length]
                sublist.append(current_value)
                product *= current_value
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
                current_index += 1
    return result