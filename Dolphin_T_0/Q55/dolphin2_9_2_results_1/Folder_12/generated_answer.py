def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == -18:
                temp = []
                k = j % size
                while i != k:
                    temp.append(lst[k])
                    k = (k + 1) % size
                    if product / lst[k] == -18:
                        result.append(temp)
    return result