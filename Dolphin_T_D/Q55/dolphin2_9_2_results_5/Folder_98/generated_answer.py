def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            if product == -1:
                if i == 0 and j == n - 1:
                    result.append(lst[i:j + 1])
                elif i == 0:
                    result.append(lst[i:j + 1] + lst[0])
                else:
                    result.append(lst[i:j + 1])
            if lst[j] == 1 or lst[j] == -1:
                continue
            if lst[j] > 1:
                product *= lst[j]
                if product > -1:
                    while product % lst[j] == 0:
                        product /= lst[j]
            else:
                product *= lst[j]
                if product < -1:
                    while product % lst[j] == 0:
                        product /= lst[j]
    return result