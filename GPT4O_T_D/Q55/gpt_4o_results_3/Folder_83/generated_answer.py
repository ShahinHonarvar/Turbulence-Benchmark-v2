def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == -57:
                sub_list = []
                for i in range(start, end + 1):
                    sub_list.append(circular_list[i % n])
                result.append(sub_list)
    return result