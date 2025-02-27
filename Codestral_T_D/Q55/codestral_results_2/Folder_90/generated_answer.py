def lists_with_product_equal_n(cir_list):
    subs = []
    n = len(cir_list)
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= cir_list[j]
            if prod == -690:
                subs.append(cir_list[i:j + 1])
    return subs