def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product_set = set()
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == 91:
                result.append(lst[i:j + 1])
            if product in product_set:
                temp_list = lst[i:j + 1]
                temp_list = temp_list[::-1]
                result.append(temp_list)
            product_set.add(product)
    return result