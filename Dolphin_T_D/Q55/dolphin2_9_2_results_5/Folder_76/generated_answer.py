def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    product_set = set()
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= circular_list[j]
            if product not in product_set:
                product_set.add(product)
                if product == 247:
                    result.append(circular_list[i:j + 1])
            if product > 247:
                break
    return result