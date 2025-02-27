def lists_with_product_equal_n(lst):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(1, length + 1):
            sublist = lst[i:i + j]
            if j > length:
                sublist += lst[:j - length]
            if product(sublist) == 27:
                result.append(sublist)
    return result