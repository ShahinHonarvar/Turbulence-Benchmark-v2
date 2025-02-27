def lists_with_product_equal_n(circular_list):
    n = 40
    result = []
    circular_list += circular_list
    for i in range(len(circular_list) // 2):
        product = 1
        for j in range(i, len(circular_list) // 2 + i):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[i:j + 1])
            if product > n:
                break
    return result