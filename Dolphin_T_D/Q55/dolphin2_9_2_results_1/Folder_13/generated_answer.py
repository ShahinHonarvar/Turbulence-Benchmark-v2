def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = lst[i:j + 1]
            product = 1
            for k in sublist:
                product *= k
            if product == 54:
                result.append(sublist)
    product_indices = []
    for i in range(n):
        if 54 % lst[i] == 0:
            product_indices.append(i)
    if len(product_indices) > 1:
        for i in range(len(list_indices)):
            for j in range(i + 1, len(list_indices)):
                if product_indices[j] == product_indices[i] + 1 or product_indices[j] == product_indices[i] - 1:
                    result.append(lst[product_indices[i]:product_indices[j]])
    return result