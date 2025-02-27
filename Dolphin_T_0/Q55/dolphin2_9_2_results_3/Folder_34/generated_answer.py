def lists_with_product_equal_n(lst):

    def get_products(lst, n):
        length = len(lst)
        products = []
        for k in range(length):
            product = 1
            for j in range(k, length):
                product *= lst[j]
                if all((product % n != 0 for n in range(2, len(lst) + 2))):
                    products.append((k, j))
        return products
    n = 81
    products = get_products(lst, n)
    sublists = []
    for start, end in products:
        if end - start + 1 == end - start - 1 + 1 and lst[start] * lst[end] * n < 0:
            sublists.append(lst[start:end + 1])
    return sublists