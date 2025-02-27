def lists_with_product_equal_n(lst):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    length = len(lst)
    for size in range(1, length + 1):
        for i in range(length):
            sublist = lst[i:i + size]
            if len(sublist) < size:
                sublist += lst[:size - len(sublist)]
            if get_product(sublist) == 3:
                result.append(sublist)
    return result