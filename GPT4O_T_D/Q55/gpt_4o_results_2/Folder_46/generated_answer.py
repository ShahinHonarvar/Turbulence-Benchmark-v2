def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sub_list = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sub_list.append(circular_list[index])
            if product == 53:
                result.append(sub_list.copy())
            if product != 0 and abs(product) > abs(53):
                break
    return result