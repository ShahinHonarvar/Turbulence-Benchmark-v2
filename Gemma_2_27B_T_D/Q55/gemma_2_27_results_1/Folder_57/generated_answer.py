from itertools import product

def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            for p in product(nums[i:j], repeat=1):
                if reduce(lambda x, y: x * y, p) == -75:
                    sublists.append(list(p))
    return sublists