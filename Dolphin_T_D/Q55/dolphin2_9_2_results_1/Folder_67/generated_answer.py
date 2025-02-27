def lists_with_product_equal_n(lst):

    def products(lst):
        if not lst:
            return [1]
        else:
            return [1] + [lst[0] * p for p in products(lst[1:] + lst[:1])]
    lst_product = len(lst) * [i for i in lst]
    for i in range(1, len(lst) * 2):
        for j in range(i, len(lst_product)):
            for k in range(i, j + 1):
                if i == 1:
                    product = 1
                else:
                    product = 1
                    for m in range(i - 1, k - 1):
                        product *= lst_product[m]
                if product == 33:
                    return lst[j - k + 1:j + 1]
    return []