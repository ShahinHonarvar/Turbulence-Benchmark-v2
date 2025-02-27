def lists_with_product_equal_n(lst):
    lst = lst + lst[:-1]
    n = len(lst)
    products = [1] * (n + 1)
    prefix_xor = 0
    sublists = []
    for i in range(n):
        prefix_xor ^= lst[i]
        products[i + 1] = products[i] * lst[i]
        if prefix_xor % 2 == 1:
            for j in range(i + 1, n + 1):
                if products[j] % products[i] == 0 and products[j] // products[i] == -33:
                    sublists.append(lst[i:j])
    return sublists