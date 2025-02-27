def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        temp = []
        for j in range(i, i + size):
            a = j % size
            temp.append(lst[a])
            product = 1
            for p in temp:
                product *= p
            if product == -23:
                result.append(temp)
    return result