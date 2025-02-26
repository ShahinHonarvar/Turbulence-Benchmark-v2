def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            index = start
            while index <= end:
                current_index = index % n
                current_value = circular_list[current_index]
                sublist.append(current_value)
                product *= current_value
                if product == 990:
                    result.append(sublist.copy())
                    break
                if product > 990:
                    break
                index += 1
    return result