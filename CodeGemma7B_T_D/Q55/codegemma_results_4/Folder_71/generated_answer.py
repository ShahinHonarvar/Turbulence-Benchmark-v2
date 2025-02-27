def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        elements = [circular_list[i]]
        for j in range(i + 1, len(circular_list), 1):
            if product * circular_list[j] <= 47:
                product *= circular_list[j]
                elements.append(circular_list[j])
            else:
                break
        if product == 47:
            result.append(elements[:])
    return result