def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    for start in range(size):
        for end in range(start, size):
            product = 1
            for i in range(start, end + 1):
                product *= circular_list[i]
            if product == -44:
                sublist = circular_list[start:end + 1]
                result.append(sublist)
    return result if result else []