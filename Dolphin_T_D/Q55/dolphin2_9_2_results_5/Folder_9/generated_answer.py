def lists_with_product_equal_n(circular_list):
    result = []
    product = 1
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == -36:
                result.append(circular_list[i:j + 1])
    for i in range(len(circular_list)):
        for j in range(0, i):
            product = 1
            for k in range(i, len(circular_list)):
                product *= circular_list[k]
                if product == -36:
                    result.append(circular_list[i:k + 1] + circular_list[0:j])
    return result if result else []