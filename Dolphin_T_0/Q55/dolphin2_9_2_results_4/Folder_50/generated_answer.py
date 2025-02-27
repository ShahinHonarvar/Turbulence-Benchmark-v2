def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == j:
                if lst[i] == 1 or lst[i] == -45 or lst[i] == 45:
                    result.append([lst[i]])
            else:
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                if product == 45:
                    result.append(lst[i:j])
    return result