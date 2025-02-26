def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            current_product = 1
            for i in range(start, end + 1):
                index = i % n
                current_product *= circular_list[index]
                sublist.append(circular_list[index])
                if current_product == -3:
                    result.append(sublist.copy())
                    break
    return result