def lists_with_product_equal_n(circ):
    for i in range(len(circ)):
        for j in range(i + 1, len(circ)):
            product = circ[i]
            for k in range(j, len(circ)):
                product *= circ[k]
                if product == -938:
                    return [circ[i:k + 1]]
                if product > -938:
                    break
    return []