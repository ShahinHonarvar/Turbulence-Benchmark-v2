def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1] + circular_list[:i]
            product = 1
            for num in sublist:
                product *= num
            if product == 49:
                result.append(sublist)
    return result