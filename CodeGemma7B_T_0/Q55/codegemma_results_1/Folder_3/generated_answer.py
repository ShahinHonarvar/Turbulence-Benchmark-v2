def lists_with_product_equal_n(circ):
    for i in range(len(circ)):
        for j in range(i + 1, len(circ)):
            product = circ[i]
            for k in range(j, len(circ)):
                product *= circ[k]
                if product == -22:
                    return [[circ[i], circ[k]]]
                elif product > -22:
                    break
    return []