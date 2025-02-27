def lists_with_product_equal_n(circular_list):
    target = 714
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == target:
                result.append(circular_list[i:j + 1])
            elif product > target:
                break
    return result