def lists_with_product_equal_n(circular_list):
    n = 5
    results = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_element = circular_list[current_index % list_length]
                sublist.append(current_element)
                product *= current_element
                if product == n:
                    results.append(sublist.copy())
                    break
                if product > n:
                    break
                current_index += 1
    return results