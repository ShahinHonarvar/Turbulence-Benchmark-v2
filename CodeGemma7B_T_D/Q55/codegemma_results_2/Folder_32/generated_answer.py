from itertools import product

def lists_with_product_equal_n(circular_list):
    products = {}
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == 76:
                products.setdefault(tuple(circular_list[i:j + 1]), []).append(i)
    sublists = []
    for sublist, indices in products.items():
        for i, j in product(indices, repeat=2):
            if i != j:
                sublists.append([circular_list[k] for k in range(i, j + 1)])
    return sublists