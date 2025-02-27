def lists_with_product_equal_n(lst):
    target_product = -95
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == target_product:
                sublist = lst[i:i + j + 1]
                if i + j + 1 > n:
                    sublist += lst[:i + j + 1 - n]
                result.append(sublist)
            elif product > abs(target_product):
                break
    return result