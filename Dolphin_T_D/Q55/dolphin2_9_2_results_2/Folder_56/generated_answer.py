def lists_with_product_equal_n(lst, n=-65):

    def get_product(sublst):
        p = 1
        for num in sublst:
            p *= num
        return p
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if get_product(lst[i:j]) == n:
                sublists.append(lst[i:j])
    return sublists