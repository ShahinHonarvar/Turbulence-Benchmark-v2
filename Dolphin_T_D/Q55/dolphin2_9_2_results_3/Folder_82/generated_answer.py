def lists_with_product_equal_n(lst):

    def is_product_equal_n(lst, n):
        product = 1
        for num in lst:
            product *= num
        return product == n
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if is_product_equal_n(sublist, 8):
                sublists.append(sublist)
    return sublists