def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    target_product = 632
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist[:])
            if product == 0 or product > target_product:
                break
    return result