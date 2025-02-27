def lists_with_product_equal_n(lst):
    result = []
    product = -46
    length = len(lst)
    for i in range(length):
        temp = []
        product_temp = 1
        for j in range(i, i + length):
            index = j % length
            product_temp *= lst[index]
            temp.append(lst[index])
            if product_temp > product:
                break
            elif product_temp == product:
                result.append(temp[:])
    return result