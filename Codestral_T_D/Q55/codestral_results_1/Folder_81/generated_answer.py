def lists_with_product_equal_n(cir_list):
    n = -8
    result = []
    length = len(cir_list)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= cir_list[j % length]
            if product == n:
                result.append(cir_list[i:j % length + 1])
            if product > n:
                break
    return result