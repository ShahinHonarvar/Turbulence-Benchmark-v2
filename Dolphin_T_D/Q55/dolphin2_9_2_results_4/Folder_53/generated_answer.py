def lists_with_product_equal_n(lst):

    def rotate(lst):
        return lst[-1:] + lst[:-1]

    def product_equals_n(sublst, n):
        product = 1
        for number in sublst:
            product *= number
        return product == n
    results = []
    for i in range(len(lst)):
        while len(lst) < 2:
            lst = rotate(lst)
        for j in range(2, len(lst) + 1):
            product = 1
            for k in range(j):
                product *= lst[(i + k) % len(lst)]
            if product_equals_n(lst[i:(i + j) % len(lst) + 1], -87):
                results.append(lst[i:(i + j) % len(lst) + 1])
    return results