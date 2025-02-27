from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    if not lst:
        return []
    products = {1: 0}
    sublists = []
    product = 1
    for i, n in enumerate(islice(cycle(lst), 1, len(lst) + 1)):
        product *= n
        if product not in products:
            products[product] = i
        if product == 4:
            sublists.append(list(islice(cycle(lst), i - products[product] + 1, i + 1)))
    return sublists