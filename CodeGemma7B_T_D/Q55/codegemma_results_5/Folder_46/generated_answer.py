def lists_with_product_equal_n(circ_list):
    length = len(circ_list)
    for i in range(length):
        product = circ_list[i]
        for j in range(1, length):
            if (i + j) % length == 0:
                break
            product *= circ_list[(i + j) % length]
            if product == 53:
                yield [circ_list[i + k] % length for k in range(j + 1)]