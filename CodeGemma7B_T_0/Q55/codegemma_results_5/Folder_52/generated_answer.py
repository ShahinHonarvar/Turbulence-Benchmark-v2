def lists_with_product_equal_n(circ):
    for i in range(len(circ)):
        for j in range(i + 1, len(circ)):
            product = 1
            for k in range(i, j + 1):
                product *= circ[k]
            if product == 37:
                sublist = circ[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
    return result