def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    product = 1
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == 5:
                result.append(lst[i:j + 1 % length])
    return result