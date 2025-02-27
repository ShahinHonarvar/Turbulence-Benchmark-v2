def lists_with_product_equal_n(lst, n=15):
    result = []
    for i in range(len(lst)):
        if lst[i] == 15:
            return [[15]]
        else:
            product = lst[i]
            for j in range(i + 1, len(lst)):
                if j == len(lst) - 1:
                    for k in range(0, i):
                        product *= lst[k]
                        if product == n:
                            result.append(lst[k:j + 1])
                        else:
                            break
                else:
                    product *= lst[j]
            for j in range(0, i):
                if j == len(lst) - 1:
                    product = lst[i]
                else:
                    product *= lst[j]
                if product == n:
                    result.append(lst[j:i + 1])
    return result