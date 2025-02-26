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
                if current_product == 25:
                    result.append(current_sublist.copy())
                if current_product > 25:
                    break
    return result