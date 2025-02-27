def lists_with_product_equal_n(circ_list):
    res = []
    n = len(circ_list)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circ_list[(i + j) % n]
            if product == 3:
                res.append(circ_list[i:i + j + 1])
                product = 1
    return res