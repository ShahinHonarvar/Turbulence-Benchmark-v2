def lists_with_product_equal_n(circular_list):
    target_product = -32
    result = []
    for _ in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[j]
            if product == target_product:
                result.append(circular_list[:j + 1])
            elif product == 0:
                break
        circular_list = circular_list[1:] + circular_list[:1]
    for length in range(1, len(circular_list)):
        for i in range(len(circular_list)):
            sublist = circular_list[i:i + length]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    return result