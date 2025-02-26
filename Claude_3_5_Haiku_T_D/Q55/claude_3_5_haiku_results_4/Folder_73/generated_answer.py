def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                element = circular_list[current_index % n]
                sublist.append(element)
                product *= element
                if product == 40:
                    result.append(sublist.copy())
                    break
                current_index += 1
    return result