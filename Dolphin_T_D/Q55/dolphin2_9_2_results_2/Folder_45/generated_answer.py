def lists_with_product_equal_n(lst):
    n = len(lst)
    for i in range(n):
        if lst[i - 1] == 1 and lst[n - 1] == -5:
            for j in range(i, n + i):
                product = 1
                for k in range(j, n + j):
                    product *= lst[k % n]
                    if product == -5:
                        return [lst[j:k + 1]]
    return []