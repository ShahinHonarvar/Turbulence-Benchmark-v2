def lists_with_product_equal_n(circular_list):
    target = 247
    result = []
    n = len(circular_list)
    circular_list = circular_list + circular_list
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j]
            if product == target:
                result.append(circular_list[i:j + 1])
            if product > target:
                break
    return result