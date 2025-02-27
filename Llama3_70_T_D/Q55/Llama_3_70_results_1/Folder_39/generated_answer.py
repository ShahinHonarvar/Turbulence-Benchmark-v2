def lists_with_product_equal_n(lst):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    result = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = lst[i:i + size]
            if len(sublist) < size:
                sublist += lst[:size - len(sublist)]
            if product(sublist) == -46:
                result.append(sublist)
    return result