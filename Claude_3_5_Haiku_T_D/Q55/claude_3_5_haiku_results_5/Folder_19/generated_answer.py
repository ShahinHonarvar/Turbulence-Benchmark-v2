def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_element = circular_list[current_index % n]
                sublist.append(current_element)
                product *= current_element
                current_index += 1
            if product == -54 and len(sublist) > 0 and (len(sublist) <= n):
                results.append(sublist)
    return results