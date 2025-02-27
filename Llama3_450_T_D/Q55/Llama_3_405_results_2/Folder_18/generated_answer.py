def lists_with_product_equal_n(circular_list):
    target_product = 36
    n = len(circular_list)
    double_list = circular_list + circular_list
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= double_list[j]
            if product == target_product:
                result.append(double_list[i:j + 1])
            elif product > target_product:
                break
    return result