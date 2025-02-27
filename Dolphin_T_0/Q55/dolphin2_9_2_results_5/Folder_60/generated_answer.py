def lists_with_product_equal_n(list_n, n=49):
    result = []
    size = len(list_n)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            sublist = list_n[j % size]
            product *= sublist
            if product == n:
                result.append(list_n[i:j % size + 1])
    return result