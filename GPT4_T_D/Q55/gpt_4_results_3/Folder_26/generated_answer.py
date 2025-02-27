def lists_with_product_equal_n(circular_list):
    circular_list.extend(circular_list)
    result = []
    for i in range(len(circular_list) // 2):
        for j in range(i, len(circular_list) // 2):
            sublist = circular_list[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 93:
                result.append(sublist[:len(sublist) - len(circular_list) // 2])
    return result