def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        temp = []
        for j in range(i, i + size):
            product *= lst[j % size]
            temp.append(lst[j % size])
            if product == -690:
                result.append(temp.copy())
    return result