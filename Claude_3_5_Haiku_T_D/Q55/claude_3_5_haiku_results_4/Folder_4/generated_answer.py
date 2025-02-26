def lists_with_product_equal_n(circular_list):
    n = 91
    result = []
    size = len(circular_list)
    for start in range(size):
        for end in range(start, start + size):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                actual_index = current_index % size
                sublist.append(circular_list[actual_index])
                product *= circular_list[actual_index]
                current_index += 1
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
    return result