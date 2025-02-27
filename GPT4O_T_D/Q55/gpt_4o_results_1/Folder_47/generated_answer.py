def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sub_list = []
        for j in range(n):
            index = (i + j) % n
            sub_list.append(circular_list[index])
            product *= circular_list[index]
            if product == -94:
                result.append(sub_list[:])
            if abs(product) >= abs(-94):
                break
    return result