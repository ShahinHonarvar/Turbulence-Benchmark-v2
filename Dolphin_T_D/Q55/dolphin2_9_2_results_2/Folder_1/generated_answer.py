def lists_with_product_equal_n(lst, n=-51):

    def comb_product(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product
    result = []
    for i in range(len(lst)):
        product = lst[i]
        if product == n:
            result.append([lst[i]])
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if comb_product(lst[i:j + 1]) == n:
                result.append(lst[i:j + 1])
    return result