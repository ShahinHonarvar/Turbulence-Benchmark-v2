def lists_with_product_equal_n(circular_list):
    n = 15
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_elem = circular_list[current_index % length]
                sublist.append(current_elem)
                product *= current_elem
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
                current_index += 1
    return result