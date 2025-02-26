def lists_with_product_equal_n(circular_list):
    n = 54
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                idx = current_index % length
                sublist.append(circular_list[idx])
                product *= circular_list[idx]
                current_index += 1
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
    return result