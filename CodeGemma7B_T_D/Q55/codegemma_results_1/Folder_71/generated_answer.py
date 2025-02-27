from functools import reduce
        from itertools import accumulate, product

def lists_with_product_equal_n(nums):
    """
        Jayanti's solution
        a = [a*b*c for a, b, c in product(nums, repeat=3) if a*b*c == n]
        """
    products = accumulate(nums, func=lambda x, y: x * y)
    windows = [list(p) for l, r in zip(products, products[1:]) for p in product(l, r) if p[0] * p[1] == 47]
    '\n        Sum and check for n = 47;\n        nums = [10, 4, -6, -2, 4, 4, 5, 80]\n          l   r    p[0]*p[1]\n        0  1    47\n        0  2    74\n        0  3    26\n        1  2    98\n        1  3    39\n        2  3    28\n        '
    return windows