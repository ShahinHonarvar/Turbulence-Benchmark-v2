def lists_with_product_equal_n(circ_list):
    circ_list *= 2
    for i in range(len(circ_list)):
        for j in range(i, len(circ_list)):
            product = 1
            for k in range(i, j + 1):
                product *= circ_list[k]
            if product == -93:
                return [circ_list[i:j + 1]]
    return []