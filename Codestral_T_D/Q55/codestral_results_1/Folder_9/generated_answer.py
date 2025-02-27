def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == -36:
                result.append(lst[i:j % length + 1])
            if product == 0:
                break
    return result