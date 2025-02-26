def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = []
            product = 1
            for k in range(j):
                current_index = (i + k) % n
                sublist.append(lst[current_index])
                product *= lst[current_index]
            if product == -82:
                result.append(sublist)
    return result