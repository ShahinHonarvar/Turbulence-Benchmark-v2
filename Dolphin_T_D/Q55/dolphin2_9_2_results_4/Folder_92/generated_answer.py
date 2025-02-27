def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = len(lst)
    result = []
    product_set = set()
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product % 5 == 0 and product != 0:
                temp = product_set.copy()
                temp.add(product)
                result.append(lst[i:j + 1])
                product_set = temp
    return result