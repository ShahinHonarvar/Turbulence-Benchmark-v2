def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            index = j % length
            product *= lst[index]
            if product == 53:
                result.append(lst[i:index + 1])
    return result