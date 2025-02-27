def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -5:
                sublist = [lst[(i + k) % len(lst)] for k in range(j + 1)]
                result.append(sublist)
            elif product > -5 and -5 % product != 0:
                break
            elif product < -5 and -5 % product == 0:
                break
    return result