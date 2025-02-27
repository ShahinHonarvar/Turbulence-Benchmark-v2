def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        sublist = [lst[i]]
        for j in range(1, n):
            j_index = (i + j) % n
            product *= lst[j_index]
            sublist.append(lst[j_index])
            if product == -5:
                result.append(sublist[:])
    return result