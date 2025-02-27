def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product_set = {1}
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product in product_set:
                result.append(lst[i:j + 1])
            else:
                product_set.add(product)
        product *= lst[i]
        if product in product_set:
            result.append(lst[i:n] + lst[:j + 1])
    return result