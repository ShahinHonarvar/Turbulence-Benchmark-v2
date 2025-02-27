def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = lst[i]
        if product == -57:
            result.append([lst[i]])
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == -57:
                result.append(lst[i:j + 1])
            elif product > -57:
                break
    return result