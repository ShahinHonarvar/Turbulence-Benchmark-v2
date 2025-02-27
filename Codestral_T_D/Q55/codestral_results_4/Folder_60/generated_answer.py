def lists_with_product_equal_n(circ_list):
    n = 49
    len_list = len(circ_list)
    circ_list += circ_list
    result = []
    for i in range(len_list):
        for j in range(i, i + len_list):
            product = 1
            for k in range(i, j + 1):
                product *= circ_list[k]
                if product == n:
                    result.append(circ_list[i:j + 1])
                elif product > n:
                    break
    return result