def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            current_sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                current_sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == 85:
                    result.append(current_sublist.copy())
                elif product > 85:
                    break
    return result