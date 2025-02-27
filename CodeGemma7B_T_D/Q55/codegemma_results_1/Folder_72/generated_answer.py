from itertools import product

def lists_with_product_equal_n(lst):
    product_n = 10
    return [sublst for sublst in product(lst, repeat=len(lst)) if product_n == reduce(lambda x, y: x * y, sublst)]