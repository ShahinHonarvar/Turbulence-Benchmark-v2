def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product_target = -968
    for i in range(n):
        product = 1
        start_index = i
        while product:
            for j in range(start_index, start_index + n):
                product *= lst[j % n]
                if product == product_target:
                    sublist = lst[start_index:j + 1]
                    result.append(sublist)
            start_index += 1
            product = 1
    return result