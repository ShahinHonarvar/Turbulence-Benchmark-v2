def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        if lst[i] == 0:
            if i < n - 1:
                if lst[i + 1] == 0 or lst[i - 1] == 0:
                    result.append([0, 0])
        else:
            for j in range(i, i + n):
                product *= lst[j % n]
                if product == -65:
                    result.append(lst[i:j + 1])
    return result