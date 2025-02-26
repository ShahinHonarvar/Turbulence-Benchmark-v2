def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            current_sublist = []
            current_product = 1
            for i in range(start, end + 1):
                index = i % n
                current_sublist.append(circular_list[index])
                current_product *= circular_list[index]
                if current_product == 247:
                    result.append(current_sublist.copy())
                    break
                if current_product > 247:
                    break
    return result