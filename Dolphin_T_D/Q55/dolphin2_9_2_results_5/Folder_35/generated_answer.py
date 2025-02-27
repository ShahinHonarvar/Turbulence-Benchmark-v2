def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        if lst[i] == 83:
            result.append([lst[i]])
        else:
            product = lst[i]
            for j in range(i + 1, n):
                product *= lst[j]
                if product == 83:
                    result.append(lst[i:j + 1])
                elif product > 83:
                    break
            for j in range(i + 1, n):
                product /= lst[j]
                if product == 83:
                    result.append(lst[i:j])
    return result