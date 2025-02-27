def lists_with_product_equal_n(lst):

    def is_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -23
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(1, length + 1):
            sublist = lst[i:i + j]
            if j > length // 2:
                sublist += lst[:j - length]
            if is_product_equal_n(sublist):
                result.append(sublist)
    return result