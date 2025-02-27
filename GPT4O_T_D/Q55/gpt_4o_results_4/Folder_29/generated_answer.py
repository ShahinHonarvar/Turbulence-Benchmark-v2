def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        current_list = []
        for j in range(n):
            index = (i + j) % n
            current_list.append(circular_list[index])
            product *= circular_list[index]
            if product == 15:
                result.append(current_list.copy())
            if len(current_list) == n:
                break
    return result