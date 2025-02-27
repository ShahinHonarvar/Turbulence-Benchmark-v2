def lists_with_product_equal_n(circ):
    for i in range(len(circ)):
        for j in range(i + 1, len(circ)):
            product = circ[i]
            for k in range(j, len(circ)):
                if product * circ[k] == -89:
                    return [[circ[i], circ[j], circ[k]]]
                product *= circ[k]
    return []