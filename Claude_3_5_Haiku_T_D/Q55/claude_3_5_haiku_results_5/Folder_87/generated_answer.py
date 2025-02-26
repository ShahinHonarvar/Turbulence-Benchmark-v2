def lists_with_product_equal_n(circular_list):
    n = 27
    results = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                sublist.append(circular_list[current_index % length])
                product *= circular_list[current_index % length]
                current_index += 1
                if product == n:
                    results.append(sublist.copy())
                elif product > n:
                    break
    return results