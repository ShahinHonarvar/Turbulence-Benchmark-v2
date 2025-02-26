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
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
                if product == 415:
                    result.append(sublist.copy())
                    break
                if product > 415:
                    break
                index += 1
    return result