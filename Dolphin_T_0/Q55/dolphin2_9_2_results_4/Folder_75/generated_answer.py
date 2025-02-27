def lists_with_product_equal_n(l, n=13):
    result = []
    size = len(l)

    def is_product_n(sublist):
        product = 1
        for i in sublist:
            product *= i
        return product == n

    def create_sublist(i, j):
        return l[i:j + 1] if i <= j else l[i:] + l[:j + 1]
    for i in range(size):
        for j in range(i, i + size):
            sublist = create_sublist(i, j)
            if is_product_n(sublist):
                result.append(sublist)
    return result