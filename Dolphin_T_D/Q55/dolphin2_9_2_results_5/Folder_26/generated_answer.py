def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    flag = 0
    for i in range(n):
        if lst[i] == 93:
            result.append([93])
            flag = 1
        if flag == 0:
            product = lst[i]
            for j in range(i + 1, n):
                product *= lst[(i + j) % n]
                if product == 93:
                    result.append(lst[i:j + 1])
                    product = 1
                    break
    return result