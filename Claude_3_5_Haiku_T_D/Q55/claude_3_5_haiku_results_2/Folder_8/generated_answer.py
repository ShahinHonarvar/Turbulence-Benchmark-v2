def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                index = current_index % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                current_index += 1
                if product == -41:
                    result.append(sublist.copy())
                    break
                if product > 41 or product < -41:
                    break
    return result