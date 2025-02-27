def lists_with_product_equal_n(circular_lst):
    sublists = []
    size = len(circular_lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= circular_lst[j % size]
            if product == -837:
                sublists.append(circular_lst[i:j + 1])
    return sublists