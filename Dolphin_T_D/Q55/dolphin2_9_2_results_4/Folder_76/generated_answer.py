def lists_with_product_equal_n(a_list):
    n = len(a_list)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            product = 1
            for k in range(i, j):
                product *= a_list[k % n]
            if product == 247:
                result.append(a_list[i:j])
    return result