def lists_with_product_equal_n(input_list):
    result = []
    n = len(input_list)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= input_list[j % n]
            if product == -115:
                result.append(input_list[i:j + 1])
    return result