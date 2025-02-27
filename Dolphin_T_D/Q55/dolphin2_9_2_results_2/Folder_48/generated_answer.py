def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    product_set = set()
    for i in range(size * 2):
        product = 1
        for j in range(i, i + size):
            if j < size:
                product *= lst[j]
            if product not in product_set and product == 990:
                sublist = lst[i:j + 1]
                result.append(sublist)
                product_set.add(product)
    return result