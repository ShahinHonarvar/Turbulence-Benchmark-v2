def lists_with_product_equal_n(circ_list):
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list)):
            product = circ_list[i]
            for k in range(j, len(circ_list)):
                if product * circ_list[k] == -69:
                    return [[circ_list[i], circ_list[k]]]
                product *= circ_list[k]
    return []