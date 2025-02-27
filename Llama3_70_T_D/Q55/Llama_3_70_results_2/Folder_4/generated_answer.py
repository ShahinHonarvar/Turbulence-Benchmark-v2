def lists_with_product_equal_n(lst):

    def is_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 91
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n + i):
            sublist = lst[j % n:]
            if is_product_equal_n(sublist):
                result.append(sublist)
            for k in range(j + 1, n + i):
                sublist = lst[j % n:k % n + 1]
                if is_product_equal_n(sublist):
                    result.append(sublist)
    return result