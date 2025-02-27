def lists_with_product_equal_n(n, circular_list):
    products = [1]
    for i in range(1, len(circular_list)):
        products.append(products[-1] * circular_list[i])
    indexes = [i for i, p in enumerate([products[0]] + [p1 * p2 for p1, p2 in zip(products[:-1], products[1:])] + [products[-1]]) if p == 247]
    return [circular_list[i:j + 1] for i, j in zip(indexes, indexes[1:] + [len(circular_list)])]