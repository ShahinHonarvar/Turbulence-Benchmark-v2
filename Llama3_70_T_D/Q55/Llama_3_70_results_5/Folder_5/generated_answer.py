def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        sublist = []
        product = 1
        for j in range(n):
            j_index = (i + j) % n
            sublist.append(lst[j_index])
            product *= lst[j_index]
            if product == -33:
                result.append(sublist[:])
            elif product < -33:
                break
    return result