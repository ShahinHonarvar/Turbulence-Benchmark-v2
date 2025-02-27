def lists_with_product_equal_n(circular_list):
    target_product = -18
    results = []
    circular_list = circular_list * 2
    length = len(circular_list) // 2
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                results.append(sublist)
    return results