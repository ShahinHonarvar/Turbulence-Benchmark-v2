def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    list_of_sublists = []
    product_set = set()
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == 36:
                list_of_sublists.append(circular_list[i:j + 1])
                product_set.add(tuple(circular_list[i:j + 1]))
    lists_set = [list(tuple) for tuple in product_set]
    return list_of_sublists if lists_set else []