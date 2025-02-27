def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        temp_list = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            temp_list.append(circular_list[index])
            if product == 90:
                result.append(temp_list.copy())
            if product == 0 or product > 90:
                break
    return result