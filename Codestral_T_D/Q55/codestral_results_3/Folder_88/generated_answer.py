def lists_with_product_equal_n(lst):
    n = -56
    circ_lst = lst + lst
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(circ_lst)):
            product *= circ_lst[j]
            if product == n:
                result.append(circ_lst[i:j + 1])
    return result