from itertools import combinations_with_replacement as cwr

def lists_with_product_equal_n(nums, n=-10):
    return [[a] * k for a, k in cwr(set(nums), -n)]