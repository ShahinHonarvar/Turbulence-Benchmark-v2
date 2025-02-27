def lists_with_product_equal_n(circ_list):
    for i in range(len(circ_list)):
        product = circ_list[i]
        for j in range(i + 1, len(circ_list)):
            product *= circ_list[j]
            if product == 537:
                sublist = circ_list[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
            elif product > 537:
                break
    return result