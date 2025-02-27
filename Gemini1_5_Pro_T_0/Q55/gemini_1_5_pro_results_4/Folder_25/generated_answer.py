def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n + 1]
            product = 1
            for k in sublist:
                product *= k
            if product == -32:
                sublists.append(sublist)
    return sublists