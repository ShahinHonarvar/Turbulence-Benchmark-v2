def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            if j - i < i + n + 1:
                product = 1
                for k in range(i, j):
                    product *= lst[k % n]
                if product == 33:
                    result.append(lst[i:j])
    return result