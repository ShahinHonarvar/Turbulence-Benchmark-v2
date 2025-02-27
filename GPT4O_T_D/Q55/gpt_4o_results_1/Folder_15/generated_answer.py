def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == -7:
                sublist = []
                for index in range(start, end + 1):
                    sublist.append(circular_list[index % n])
                result.append(sublist)
            if abs(product) > abs(-7):
                break
    return result