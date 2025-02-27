def lists_with_product_equal_n(lst):
    product = -94
    result = []
    length = len(lst)
    for i in range(length):
        product_temp = 1
        for j in range(i, length + i):
            product_temp *= lst[j % length]
            if product_temp == product:
                result.append(lst[j - i + 1:j + 1])
    return result