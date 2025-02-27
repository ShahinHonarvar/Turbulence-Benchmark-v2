def lists_with_product_equal_n(circ_list):
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list)):
            product = 1
            for k in range(i, j + 1):
                product *= circ_list[k]
            if product == 43:
                sublist = circ_list[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
    return result