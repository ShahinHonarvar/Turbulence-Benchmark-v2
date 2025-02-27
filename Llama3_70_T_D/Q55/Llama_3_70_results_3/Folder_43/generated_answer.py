def lists_with_product_equal_n(lst):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, i + n):
            sublist = lst[i:j % n + 1]
            if product(sublist) == -26:
                result.append(sublist)
    return result