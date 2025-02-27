def lists_with_product_equal_n(lst):

    def is_product_37(lst):
        n = len(lst)
        product = 1
        for i in range(n):
            product *= lst[i]
        return product == 37
    n = len(lst)
    subsets = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if is_product_37(lst[i:j]):
                subsets.append(lst[i:j])
    return subsets