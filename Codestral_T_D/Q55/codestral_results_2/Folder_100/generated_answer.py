def lists_with_product_equal_n(circular_list):
    n = 48
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)] + [circular_list[j % len(circular_list)]]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result